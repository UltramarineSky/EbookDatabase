import databases
from module.logging_config import LogManager
from typing import Any, List, Union

# 创建 LogManager 的实例
log_manager = LogManager('log/app.log')
# 获取 logger 实例
logger = log_manager.get_logger()


class DatabaseManager:
    def __init__(self):
        self.connections = {}

    async def connect(self, db_name: str) -> bool:
        logger.info(f"尝试连接到数据库 {db_name}")
        if db_name not in self.connections:
            try:
                db_url = f"sqlite:///instance/{db_name}.db"
                new_db = databases.Database(db_url)
                await new_db.connect()
                self.connections[db_name] = new_db
                logger.info(f"成功连接到数据库 {db_name}")
                return True
            except Exception as e:
                logger.error(f"连接数据库 {db_name} 失败: {e}")
                return False
        return False

    def get_connection(self, db_name: str):
        logger.info(f"尝试获取 {db_name} 的数据库连接")
        # 去掉扩展名（如果存在）
        db_name = db_name.replace('.db', '')
        logger.info(f"当前所有已连接的数据库：{list(self.connections.keys())}")
        return self.connections.get(db_name, None)

    async def fetch_one(self, db_name: str, query: str, values: dict) -> Union[None, dict]:
        db = self.get_connection(db_name)
        if db:
            try:
                result = await db.fetch_one(query=query, values=values)
                logger.info(f"成功执行查询: {query}")
                return result
            except Exception as e:
                logger.error(f"查询失败: {e}")
                return None
        logger.warning(f"未找到数据库 {db_name} 的连接")
        return None

    async def fetch_all(self, db_name: str, query: str, values: dict) -> List[Any]:
        db = self.get_connection(db_name)
        if db:
            try:
                result = await db.fetch_all(query=query, values=values)
                logger.info(f"成功执行查询: {query}")
                return result
            except Exception as e:
                logger.error(f"查询失败: {e}")
                return []
        logger.warning(f"未找到数据库 {db_name} 的连接")
        return []

    async def close_all(self):
        for _, db in self.connections.items():
            try:
                await db.disconnect()
                logger.info("成功关闭数据库连接")
            except Exception as e:
                logger.error(f"关闭数据库连接失败: {e}")

