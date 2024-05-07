export PYTHONPATH=.
export DATABASE=mysql+pymysql://root:password@localhost:3306/sandbox?charset=utf8mb4
python demo_ecommerce/initialization/init_data.py $DATABASE