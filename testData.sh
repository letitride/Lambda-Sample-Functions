aws dynamodb put-item --table-name mailaddress --item '{"email":{"S":"ichikawa.fumiya+1@gmail.com"}, "username":{"S":"FumiyaIchikawa1"},"haserror":{"N":"0"},"issend":{"N":"0"}}'
aws dynamodb put-item --table-name mailaddress --item '{"email":{"S":"ichikawa.fumiya+2@gmail.com"}, "username":{"S":"FumiyaIchikawa2"},"haserror":{"N":"0"},"issend":{"N":"0"}}'
aws dynamodb put-item --table-name mailaddress --item '{"email":{"S":"ichikawa.fumiya+3@gmail.com"}, "username":{"S":"FumiyaIchikawa3"},"haserror":{"N":"0"},"issend":{"N":"0"}}'
aws dynamodb put-item --table-name mailaddress --item '{"email":{"S":"ichikawa.fumiya+4@gmail.com"}, "username":{"S":"FumiyaIchikawa4"},"haserror":{"N":"0"},"issend":{"N":"0"}}'
aws dynamodb put-item --table-name mailaddress --item '{"email":{"S":"ichikawa.fumiya+5@gmail.com"}, "username":{"S":"FumiyaIchikawa5"},"haserror":{"N":"0"},"issend":{"N":"0"}}'

aws dynamodb put-item --table-name mailaddress --item '{"email":{"S":"success@simulator.amazonses.com"}, "username":{"S":"Suucess"},"haserror":{"N":"0"},"issend":{"N":"0"}}'
aws dynamodb put-item --table-name mailaddress --item '{"email":{"S":"bounce@simulator.amazonses.com"}, "username":{"S":"bounce"},"haserror":{"N":"0"},"issend":{"N":"0"}}'
aws dynamodb put-item --table-name mailaddress --item '{"email":{"S":"ooto@simulator.amazonses.com"}, "username":{"S":"ooto"},"haserror":{"N":"0"},"issend":{"N":"0"}}'
aws dynamodb put-item --table-name mailaddress --item '{"email":{"S":"complaint@simulator.amazonses.com"}, "username":{"S":"complaint"},"haserror":{"N":"0"},"issend":{"N":"0"}}'
aws dynamodb put-item --table-name mailaddress --item '{"email":{"S":"suppressionlist@simulator.amazonses.com"}, "username":{"S":"suppressionlist"},"haserror":{"N":"0"},"issend":{"N":"0"}}'
