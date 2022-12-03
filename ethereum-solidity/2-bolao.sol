pragma solidity 0.5.16;

contract Bolao {
    address private gerente;
    address[] private jogadores;
    // endereço do vencedor
    address payable private vencedor;

    constructor() public {
        // quem publicar o contrato vai ser o gerente
        gerente = msg.sender;
    }

    // event for EVM logging (bytes da string são registrados - precisa converter para ler)
    event log(address indexed novoParticipante, bytes32 indexed mensagem);

    // marcar o método como payable para indicar que existe custo além do gas
    // na interface vai aparecer um campo para digitar a qtd de ETH para transferir
    function entrar() public payable {
        // valida o valor da transação (paga 0.1 ETH para entrar)
        require(msg.value == .1 ether, "Taxa de entrada precisa ser 0.1 ETH");
        jogadores.push(msg.sender);
        emit log(msg.sender, "Entrou no bolão");
    }

    // restricted é um modificador declarado no contrato
    function descobrirGanhador() public restricted {
        uint index = randomico() % jogadores.length;
        vencedor = address(uint160(jogadores[index]));

        // transfere o valor para o vencedor
        vencedor.transfer(address(this).balance);
        jogadores = new address[](0);
        vencedor = address(uint160(0x0));
        emit log(vencedor, "Ganhou o bolão");
    }

    // declara um modificador para validar o sender
    modifier restricted() {
        emit log(vencedor, "Tentou executar o sorteio");
        // apenas quem criou o contrato pode chamar
        require(msg.sender == gerente, "Somente o gerente do bolão pode efetuar o sorteio");
        _;
    }

    function getSaldo() public view returns (uint) {
        return uint(address(this).balance);
    }

    function randomico() private view returns (uint) {
        return uint(keccak256(abi.encodePacked(block.difficulty, now, jogadores)));
    }
}
