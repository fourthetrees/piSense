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
        outfile='/home/forrest/Code/daemonOut.txt',errfile='/home/forrest/Code/daemonErr.txt')
    daemonTest.start()
    time.sleep(60)
    daemonTest.stop()

if __name__ == '__main__':
    Main()