using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class UIManager : MonoBehaviour {
    public Text goldDisplayer;
    public Text goldPerClickDisplayer;
    public Text goldPerSecDisplayer;

    void Update()
    {
        goldDisplayer.text = "COMBAT POWER: " + DataController.GetInstance().GetGold();
        goldPerClickDisplayer.text = "POWER PER CLICK: " + DataController.GetInstance().GetGoldPerClick();
        goldPerSecDisplayer.text = "POWER PER SEC: " + DataController.GetInstance().GetGoldPerSec();
    }
}
