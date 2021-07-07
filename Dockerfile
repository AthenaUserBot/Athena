FROM sandy1709/catuserbot:latest
RUN git clone https://github.com/athenauserbot/athenauserbot.git /root/athenauserbot
WORKDIR /root/athenauserbot
RUN pip3 install -U -r requirements.txt
ENV PATH="/home/athenauserbot/bin:$PATH"
CMD ["python3", "itsathena.py"]
