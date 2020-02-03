pragma solidity ^0.5.0;

contract CoinaAppart {
    address public locataire;
    address public proprietaire;
    
    bool public validationLocataire;
    //bool public validationProprietaire;
    
    uint24 public amount;
    
    bytes32 public hashDoc;
    
    constructor(address _proprietaire , bytes32  _hashDoc, uint24  _amount ) public 
    {
        locataire = msg.sender;
        proprietaire = _proprietaire;
        hashDoc = _hashDoc;
        amount = _amount;
        validationLocataire = false;
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
    
    
}