pragma solidity >=0.4.0 <0.7.0;

contract SimpleStorage {
	// tipos:
	// - boolean
	// - int2 até int256, uint2 até uint256
	// - fixedMxN e unfixedMxN
	// - bytes1 até bytes32
	// - address e address payable (apenas para pagto)
	// - enum
	// - struct
	uint storedData;

	// visibilidades: public, private, internal e external
	function set(uint x) public {
	    storedData = x;
	}

	function get() public view returns (uint) {
	    return storedData;
	}
}

