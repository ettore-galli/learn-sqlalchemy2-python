export PYTHONPATH=.
export DATABASE=mysql+pymysql://root:password@localhost:3306/sandbox?charset=utf8mb4

echo Create...
python demo_ecommerce/initialization/create.py $DATABASE
echo Init data...
python demo_ecommerce/initialization/init_data_faker.py $DATABASE