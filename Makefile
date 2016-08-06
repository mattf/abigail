graffiti:
	git reset $(git rev-list --max-parents=0 HEAD)
	./spray.py README | sh
	git push --force origin master
