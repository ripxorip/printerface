#include <Arduino.h>
#include "communication.h"

Communication::Communication()
{
}

void Communication::tx(int gasValue)
{
    /* Report Gas */
    Serial.print("{\"gas\":");
    Serial.print(gasValue);
    /* Finish line */
    Serial.print(",");
    /* Report Temperature */
    Serial.print("\"temp\":");
    Serial.print("24.2");
    Serial.print("}");
    Serial.print("\n");
}

printerface_action_t Communication::rx()
{
    printerface_action_t ret = nop;
    String inp;
    if (Serial.available())
    {
        inp = Serial.readString();
    }
    else
    {
        goto exit;
    }
    /* Process input */

exit:
    return ret;
}