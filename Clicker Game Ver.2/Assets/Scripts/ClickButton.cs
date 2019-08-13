using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ClickButton : MonoBehaviour
{
    public int gold = 0;
    public int goldPerClick = 1;

    public void OnClick()
    {
        gold += goldPerClick;
    }
}
