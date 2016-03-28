JFLAGS = -g
JC = javac
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) ExponentationBySquaring.java

CLASSES = ExponentationBySquaring.java 

default: classes

classes: $(CLASSES:.java=.class)

clean:
	$(RM) *.class

