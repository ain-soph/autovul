# Used for python interactive window

import autovul.vision


env = autovul.vision.environ.create(verbose=1, color=True, tqdm=True)
dataset = autovul.vision.datasets.create()
model = autovul.vision.models.create(dataset=dataset)
trainer = autovul.vision.trainer.create(dataset=dataset, model=model)
mark = autovul.vision.marks.create(dataset=dataset)
attack = autovul.vision.attacks.create('trojannn', dataset=dataset, model=model, mark=mark)
