#include <stdint.h>
#include <iostream>
#include <pthread.h> 

using namespace std;

bool cond_bool = false; 

pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond1 = PTHREAD_COND_INITIALIZER;

void* wait_thread(void*)
{
	pthread_mutex_lock(&mutex1);	//	pthread_cond_wait must protect by the mutex lock to avoid other thread called cond_signal before cond_wait
	while(!cond_bool)				//	recommended usage is cooperating with a while loop to avoid cond_signal called even if the condition has not fulfilled
	{
		pthread_cond_wait(&cond1, &mutex1);	//	If cond1 doesn't signaled, unlock mutex and wait
		//	proceed when cond1 signaled, and lock mutex again
	}
	pthread_mutex_unlock(&mutex1);
//	pthread_exit(NULL);
}

void* signal_thread(void*)
{
	pthread_mutex_lock(&mutex1);
	cond_bool = true;
	pthread_cond_signal(&cond1);
	pthread_mutex_unlock(&mutex1);
//	pthread_exit(NULL);
}

int main(int argc, char** argv) 
{
	pthread_t wait, signal;
	pthread_create(&wait, NULL, wait_thread, NULL);
	pthread_create(&signal, NULL, signal_thread, NULL);
	pthread_join(wait, NULL);		// Main Process wait for the wait_thread 
	pthread_join(signal, NULL); 	// MAin Process wait for the signal_thread
	return 0;
}
