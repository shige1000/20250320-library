import asyncio


class AsyncSingleton:
    _instance = None
    _lock = asyncio.Lock()

    async def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            async with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    # 非同期初期化メソッドを呼び出す場合
                    if hasattr(cls._instance, "_async_initialize"):
                        await cls._instance._async_initialize(*args, **kwargs)
                    # 同期初期化メソッドもサポートする場合
                    elif hasattr(cls._instance, "_initialize"):
                        cls._instance._initialize(*args, **kwargs)
        return cls._instance

    # 非同期用の初期化メソッド（オプション）
    # async def _async_initialize(self, *args, **kwargs):
    #     pass

    # 同期用の初期化メソッド（オプション）
    # def _initialize(self, *args, **kwargs):
    #     pass
