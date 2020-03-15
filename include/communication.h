#ifndef __COMM_H__
#define __COMM_H__

typedef enum
{
    nop,
    lights_on,
    lights_off
} printerface_action_t;

/**
 * This class is responsible for managing
 * the Rpi communication
 */
 
class Communication
{
private:

public:
    Communication();

    /* Periodically send values for e.g. smoke and temp */
    void tx(int gasValue);
    /* Receive new instructions */
    printerface_action_t rx();
};
 
#endif