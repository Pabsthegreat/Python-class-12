import pickle
lst = [
['Afghanistan', 'Kabul', '34.28N', '69.11E'],
['Albania',	'Tirane', '41.18N', '19.49E'],
['Algeria',	'Algiers', '36.42N', '03.08E'],
['Iceland',	'Reykjavik', '64.10N', '21.57W'],
['India', 'New Delhi', '28.37N', '77.13E'],
['Indonesia',  'Jakarta', '06.09S', '106.49E'] ]

def countries():
    with open ("Countries.dat",'wb') as f:
        for i in lst:
            pickle.dump(i,f)
countries()
