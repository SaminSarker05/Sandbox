run: build
	@./out
	
build: review.cpp
	@g++ -o out review.cpp

save:
	@cd ../..
	@git add .
	@git commit -a -m "progress"
	@git push

clean:
	@rm -f out