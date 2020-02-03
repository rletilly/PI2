pragma solidity ^0.5.0;

contract CoinaAppart {
    address public _locataire;
    address public _proprietaire;
    
    bool public _validationLocataire;
    bool public _validationProprietaire;
    
    uint24 public amount;
    
    bytes32 public hashDoc;
    
    constructor(address proprietaire) public 
    {
        _locataire = msg.sender;
        _proprietaire = proprietaire;
    }
    
    
    function launchContract(bytes32  hash, uint24  amount ) public returns (bool check)
    {
        if (_validationLocataire || _validationProprietaire)
        {
            
        }
        else
        {
            
        }
    }
    
    bool public _launchContract;
    
}