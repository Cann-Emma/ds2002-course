#!/bin/bash


curl https://d2r55xnwy6nx47.cloudfront.net/uploads/2024/02/DefaultModeExplainer-byKristinaArmitage-Lede-scaled.webp > rest.webp
aws s3 cp rest.webp s3://ds2002-zgb8ts

# https://s3.amazonaws.com/ds2002-zgb8ts/rest.webp

aws s3 ls s3://ds2002-zgb8ts
aws s3 presign --expires-in 604800 s3://ds2002-zgb8ts/rest.webp

#Output: https://ds2002-zgb8ts.s3.us-east-1.amazonaws.com/rest.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYS2NRLWOSPAL2AF6%2F20240229%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240229T200928Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=FwoGZXIvYXdzEDUaDIuKbTipedbkJGzwlCLEAfilQjgerVnSEZytI7EypFg%2FzTcfLl2EWuHxSHjpXU%2B%2F88REv2rPVv8EO7ySDhc6B4pW%2B2joH0z%2FtN1e5EyV13UGzJWTktBr4AMHJakDn8enol1v%2FfCTc%2BBWs4sxHYY%2BjfEl7wvLXMLRC3%2Flpz5D0qY87gOS7M6NbgrPvJauEYnNuje4Gk7BA7fWjp3hooSMM7tqknk3r8elwSK1uralaUCHM%2B%2BrSifkX7y5TJuwSIp4XOSMn37EQsBp8hj05cFEr2TpnAooqMGDrwYyLe22FkbjeWvEx8epxpNYlQ7bueKBNRMRQLkOEO31plu1cBuL3GBncy7hIcVQLw%3D%3D&X-Amz-Signature=87d2f9ec1db56c46f4ee922f5da9cee309259d7d9f2989458f7caabb278afca8

