pragma solidity ^0.5.12;

contract CEth 
{
  function mint() external payable;
  function balanceOf(address owner) external view returns (uint256);
  function redeem(uint redeemTokens) external returns (uint);
}

//########################################################
//####   MAIN CONTRACT                              ######
//########################################################

contract  CoinAppart {
   
    //########################################################
    //####   Global Variables                           ######
    //########################################################
    address payable public locataire;
    address public proprietaire;
    address payable public ethCompound = address(uint160(0x001d70b01a2c3e3b2e56fcdcefe50d5c5d70109a5d));
    bool public validationLocataire;
    uint public Amount;
    uint public cAmount;
    bytes32 public hashDoc;
    //bool public validationProprietaire;
    
    /*
    constructor(address _proprietaire , bytes32  _hashDoc) public payable
    {
        locataire = msg.sender;
        proprietaire = _proprietaire;
        hashDoc = _hashDoc;
        amount = msg.value;
        validationLocataire = true;
    }
    */ //Completed Constructor
    constructor() public payable
    {
        locataire = msg.sender;
        //proprietaire = _proprietaire;
        //hashDoc = _hashDoc;
        Amount = msg.value;
        validationLocataire = true;
    }
    
    
    function launchContract(bytes32  _hashDoc, uint24 _amount ) public returns (bool check)
    {
        require(msg.sender == proprietaire);
        if(_hashDoc == hashDoc && Amount == _amount)
        {
            validationLocataire = true;
            check = true;
        }
        else
        {
            check = false;
        }
        return check;
    }
    
    //########################################################
    //####   Compound communication Functions           ######
    //########################################################
    
    //Send eth to compound to get CEth

    function sendToCompound() public returns (bool check)
    {
        CEth(ethCompound).mint.value(address(this).balance).gas(250000)();
        return true;
    }
    
    function getBackFromCompound() public returns (bool check)
    {
        CEth(ethCompound).redeem.gas(400000)(cAmount);
        return true;
    }
    function update_cToken() public returns (bool check)
    {
        cAmount = getBalance_cToken();
        return true;

    }
    
    
    //########################################################
    //####              View Functions                  ######
    //########################################################
    //See how much cEth we own 
    function getBalance_cToken() public view returns (uint){return CEth(ethCompound).balanceOf(address(this));}
    //Able me to see how much eth the contract own
    function getBalance_Token()public view returns (uint){return address(this).balance;}
    
    
}