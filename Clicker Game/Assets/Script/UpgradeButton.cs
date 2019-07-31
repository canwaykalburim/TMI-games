using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class UpgradeButton : MonoBehaviour {

    public Text upgradeDisplayer;

    public string upgradeName;

    [HideInInspector]

    public int goldByUpgrade;
    public int startGoldByUpgrade = 10;

    [HideInInspector]

    public int currentCost = 1;
    public int startCurrentCost = 1;

    [HideInInspector]

    public int level = 1;

    public float upgradePow = 10.25f;
    public float costPow = 0.2f;

    public DataController dataController;

    void Start()
    {
        DataController.GetInstance().LoadUpgradeButton(this);
            UpdateUI();
    }

    public void PurChaseUpgrade()
    {
        if (DataController.GetInstance().GetGold() >= currentCost)
        {
            DataController.GetInstance().SubGold(currentCost);
            level++;
            DataController.GetInstance().AddGoldPerClick(goldByUpgrade);

            UpdateUpgrade();
            UpdateUI();
            DataController.GetInstance().SaveUpgradeButton(this);
        }
    }

    public void UpdateUpgrade()
    {
        goldByUpgrade += startGoldByUpgrade * (int) Mathf.Pow(upgradePow, level);
        currentCost = startCurrentCost * (int)Mathf.Pow(costPow, level);
    }

    public void UpdateUI()
    {
        upgradeDisplayer.text = upgradeName + "\nCost: " + currentCost + "\nlevel:" + level +
            "\nNext GoldPerClick:" + goldByUpgrade;
    }
}