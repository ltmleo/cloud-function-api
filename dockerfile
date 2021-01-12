FROM public.ecr.aws/lambda/python:3.6

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "src.main.list_customers_by_total_handler" ]
