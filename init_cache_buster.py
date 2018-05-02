from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask_cache_buster import CacheBuster

app = Flask(__name__)

config = {
     'extensions': ['.js', '.css', '.csv'],
     'hash_size': 10
}

cache_buster = CacheBuster(config=config)
cache_buster.register_cache_buster(app)
