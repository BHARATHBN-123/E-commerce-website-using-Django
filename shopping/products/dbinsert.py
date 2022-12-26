from .models import product
import names
import pandas as pd


def inserttoproduct():
    for i in range(0, 101):
        a = pd.read_csv("products\submission.csv")
        p = product.objects.create(item=names.get_first_name(),
                                   content=str(a['selected_text'][i]), price=i+100)
        p.save()


inserttoproduct()
