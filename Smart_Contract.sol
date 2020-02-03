pragma solidity ^0.5.0;

contract CoinaAppart {
    address public locataire;
    address public proprietaire;
    
    bool public validationLocataire;
    //bool public validationProprietaire;
    
    uint24 public amount;
    
    bytes32 public hashDoc;
    
    constructor() public 
    {
        locataire = msg.sender;
    }
    
    function initializationContract(address _proprietaire , bytes32  _hashDoc, uint24  _amount ) public returns (bool)
    {
        require(msg.sender == locataire);
        proprietaire = _proprietaire;
        hashDoc = _hashDoc;
        amount = _amount;
        validationLocataire = false;
        return true;
    }
    
    
    function launchContract(bytes32  _hashDoc, uint24 _amount ) public returns (bool check)
    {
        require(msg.sender == proprietaire);
        if(_hashDoc == hashDoc && amount == _amount)
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
    
    function getLocataire() view public returns (address){
        return locataire;
    }
    function getProprietaire() view public returns (address){
    return proprietaire;
    }
    function getAmount() view public returns (uint24){
    return amount;
    }
    
}