import sys, time, daemon

class someDaemon(daemon.daemon):

    def loop(self):
        while True:
            print('Daemon Running at Time: {0}'.format(time.time()))
            sys.stdout.flush()
            time.sleep(10)

    def run(self):
        self.loop()

def Main():
    daemonTest = someDaemon('/tmp/raspiDaemonTest.pid',
        outfile='~/piSense/tmp/daemon/daemonOut.txt',
        errfile='~/piSense/tmp/daemon/daemonErr.txt')
    daemonTest.start()

if __name__ == '__main__':
    Main()