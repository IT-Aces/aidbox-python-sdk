import logging
import coloredlogs
from aiohttp import web

from aidbox_python_sdk.main import run_standalone_app
from aidbox_python_sdk.settings import Settings
from aidbox_python_sdk.manifest import Manifest

coloredlogs.install(level='DEBUG', fmt='%(asctime)s %(levelname)s %(message)s')

settings = Settings(**{})
manifest = Manifest(settings)


def main():
    logging.info('Started')
    run_standalone_app(settings, manifest, debug=True)


"""
Test REST requests for subs and ops:
POST /User
POST /Patient

POST /signup/register?param1=123&param2=foo
GET /Patient/$daily-report?param=papam
POST /User/$register
"""


@manifest.subscription('User')
async def user_sub(event):
    logging.debug('`User` subscription handler')
    logging.debug('Event: {}'.format(event))
    return web.json_response({})


@manifest.subscription(entity='Patient')
def patient_sub(event):
    logging.debug('`Patient` subscription handler')
    logging.debug('Event: {}'.format(event))
    return web.json_response({})


@manifest.operation(method='POST', path=['signup', 'register'])
def signup_register_op(operation, params):
    logging.debug('`signup_register_op` operation handler')
    logging.debug('Operation data: {}'.format(operation))
    logging.debug('Url params: {}'.format(params))
    return web.json_response({})


@manifest.operation(method='GET', path=['Patient', '$daily-report'])
async def daily_patient_report(operation, params):
    logging.debug('`daily_patient_report` operation handler')
    logging.debug('Operation data: {}'.format(operation))
    logging.debug('Url params: {}'.format(params))
    return web.json_response({})


@manifest.operation(method='POST', path=['User', '$register'])
async def register_user(operation, params):
    logging.debug('`register_user` operation handler')
    logging.debug('Operation data: {}'.format(operation))
    logging.debug('Url params: {}'.format(params))
    return web.json_response({})


if __name__ == '__main__':
    main()
