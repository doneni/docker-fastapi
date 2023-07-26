import uvicorn
from app import app

if __name__ == '__main__':
    try:
        uvicorn.run(
            "main:app",
            host='0.0.0.0',
            port=8080,
            workers=5,
            log_level='warning',
            reload=False,
        )
    except KeyboardInterrupt:
        print('\nExiting\n')
    except Exception as errormain:
        print('Failed to Start API')
        print('='*100)
        print(str(errormain))
        print('='*100)
        print('Exiting\n')
