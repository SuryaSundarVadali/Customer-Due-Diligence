// SPDX-License-Identifier: None
pragma solidity 0.8.7;

import '@chainlink/contracts/src/v0.8/ChainlinkClient.sol';

contract AdvancedIdentityVerification is ChainlinkClient{

    string walletID;
    mapping(string=>uint256) public verifyAddress;

    using Chainlink for Chainlink.Request;

    uint256 private value;
    bytes32 private jobId;
    uint256 private fee;

    event RequestValue(bytes32 indexed requestId, uint256 value);

    constructor(){
        setChainlinkToken(0x326C977E6efc84E512bB9C30f76E30c160eD06FB);
        setChainlinkOracle(0xCC79157eb46F5624204f47AB42b3906cAA40eaB7);
        jobId = 'ca98366cc7314957b8c012c72f05aeeb';
        fee = (1 * LINK_DIVISIBILITY) / 10; // 0,1 * 10**18 (Varies by network and job)
    }

    function requestValueData(string memory _path) public returns (bytes32 requestId){
        walletID = _path;
        Chainlink.Request memory req = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);
        req.add('get', 'https://plum-busy-cuttlefish.cyclic.app/');
        req.add('path', _path);
        int256 timesAmount = 1;
        req.addInt('times', timesAmount);
        return sendChainlinkRequest(req, fee);
    }

    function fulfill(bytes32 _requestId, uint256 _value) public recordChainlinkFulfillment(_requestId) {
        emit RequestValue(_requestId, _value);
        value = _value;
        verifyAddress[walletID] = _value;
    }

    function withdrawLink() public {
        LinkTokenInterface link = LinkTokenInterface(chainlinkTokenAddress());
        require(link.transfer(msg.sender, link.balanceOf(address(this))), 'Unable to transfer');
    }

}