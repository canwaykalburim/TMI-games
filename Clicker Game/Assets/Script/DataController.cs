using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DataController : MonoBehaviour {

    private static DataController instance;

    public static DataController GetInstance()
    {
        if (instance == null)
        {
            instance = FindObjectOfType<DataController>();

            if (instance == null)
            {
                GameObject container = new GameObject("DataController");

                instance = container.AddComponent<DataController>();
            }
        }
        return instance;
    }

    private int m_Gold = 0;
    private int m_GoldPerClick = 0;

    void Awake()
    {
        m_Gold = PlayerPrefs.GetInt("Gold");
        m_GoldPerClick = PlayerPrefs.GetInt("GoldPerClick", 1);
    }

    public void SetGold(int NewGold)
    {
        m_Gold = NewGold;
        PlayerPrefs.SetInt("Gold", m_Gold);
    }

    public void AddGold(int NewGold)
    {
        m_Gold += NewGold;
        SetGold(m_Gold);
    }

    public void SubGold(int NewGold)
    {
        m_Gold -= NewGold;
        SetGold(m_Gold);
    }

    public int GetGold()
    {
       return m_Gold;
    }

    public int GetGoldPerClick()
    {
        return m_GoldPerClick;
    }

    public void SetGoldPerClick(int newGoldPerClick)
    {
        m_GoldPerClick = newGoldPerClick;
        PlayerPrefs.SetInt("GoldPerClick", m_GoldPerClick);
    }

    public void AddGoldPerClick(int newGoldPerClick)
    {
        m_GoldPerClick += newGoldPerClick;
        SetGoldPerClick(m_GoldPerClick);
    }

    public void LoadUpgradeButton(UpgradeButton upgradeButton)
    {
        string key = upgradeButton.upgradeName;
        upgradeButton.level = PlayerPrefs.GetInt(key + "_level", 1);
        upgradeButton.goldByUpgrade = PlayerPrefs.GetInt(key + "_goldByUpgrade", upgradeButton.startGoldByUpgrade);
        upgradeButton.currentCost = PlayerPrefs.GetInt(key + "_cost", upgradeButton.startCurrentCost);
    }

    public void SaveUpgradeButton(UpgradeButton upgradeButton)
    {
        string key = upgradeButton.upgradeName;
        PlayerPrefs.SetInt(key + "_level", upgradeButton.level);
        PlayerPrefs.SetInt(key + "_goldByUpgrade", upgradeButton.goldByUpgrade);
        PlayerPrefs.SetInt(key + "_cost", upgradeButton.currentCost);
    }

    public void LoadItemButton(ItemButton itemButton)
    {
        string key = itemButton.itemName;

        itemButton.level = PlayerPrefs.GetInt(key + "_level");
        itemButton.currentCost = PlayerPrefs.GetInt(key + "_cost", itemButton.startCurrentCost);
        itemButton.goldPerSec = PlayerPrefs.GetInt(key + "_goldPerSec");

        if (PlayerPrefs.GetInt(key + "_isPurchased") == 1)
        {
            itemButton.isPurchased = true;
        }
        else
        {
            itemButton.isPurchased = false;
        }
    }

    public void SaveItemButton(ItemButton itemButton)
    {
        string key = itemButton.itemName;

        PlayerPrefs.SetInt(key + "_level", itemButton.level);
        PlayerPrefs.SetInt(key + "_cost", itemButton.currentCost);
        PlayerPrefs.SetInt(key + "_goldPerSec", itemButton.goldPerSec);

        if (itemButton.isPurchased == true)
        {
            PlayerPrefs.SetInt(key + "_isPurchased", 1);
        }
        else
        {
            PlayerPrefs.SetInt(key + "_isPurchased", 0);
        }
    }
}