import asyncio


class AsyncSingleton:
    _instance = None
    _lock = asyncio.Lock()

    async def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            async with cls._lock:
                if cls._instance is None:
                    print(f"Creating instance of {cls.__name__}")  # デバッグ用
                    cls._instance = super().__new__(cls)
                    # 非同期初期化メソッドを呼び出す場合
                    if hasattr(cls._instance, "_async_initialize"):
                        print(f"Calling _async_initialize for {cls.__name__}")  # デバッグ用
                        await cls._instance._async_initialize(*args, **kwargs)
                    # 同期初期化メソッドもサポートする場合
                    elif hasattr(cls._instance, "_initialize"):
                        print(f"Calling _initialize for {cls.__name__}")  # デバッグ用
                        cls._instance._initialize(*args, **kwargs)
        else:
            print(f"Returning existing instance of {cls.__name__}")  # デバッグ用
        return cls._instance

    @classmethod
    async def get_instance(cls, *args, **kwargs):
        if cls._instance is None:
            async with cls._lock:
                if cls._instance is None:
                    instance = cls()
                    # 初期化後に代入する（ここが重要！）
                    if hasattr(instance, "_async_initialize"):
                        await instance._async_initialize(*args, **kwargs)
                    elif hasattr(instance, "_initialize"):
                        instance._initialize(*args, **kwargs)
                    cls._instance = instance
        return cls._instance

    # 非同期用の初期化メソッド（オプション）
    # async def _async_initialize(self, *args, **kwargs):
    #     pass

    # 同期用の初期化メソッド（オプション）
    # def _initialize(self, *args, **kwargs):
    #     pass
