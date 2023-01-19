#!/bin/bash

speedtest --accept-license --accept-gdpr | grep 'Download\|Upload' | awk '{print $2,$3}'
