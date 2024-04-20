export PYTHONPATH=.
export DATABASE=mysql+pymysql://root:password@localhost:3306/sandbox?charset=utf8mb4

echo Create...
python demo_ecommerce/models/create.py $DATABASE
echo Init data...
python demo_ecommerce/models/init_data_faker.py $DATABASE