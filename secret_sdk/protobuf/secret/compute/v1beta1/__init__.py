# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: secret/compute/v1beta1/genesis.proto, secret/compute/v1beta1/msg.proto, secret/compute/v1beta1/query.proto, secret/compute/v1beta1/types.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ....cosmos.base import v1beta1 as ___cosmos_base_v1_beta1__
from ....cosmos.base.abci import v1beta1 as ___cosmos_base_abci_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class AccessType(betterproto.Enum):
    UNDEFINED = 0
    NOBODY = 1
    ONLY_ADDRESS = 2
    EVERYBODY = 3


@dataclass(eq=False, repr=False)
class AccessTypeParam(betterproto.Message):
    value: "AccessType" = betterproto.enum_field(1)


@dataclass(eq=False, repr=False)
class CodeInfo(betterproto.Message):
    """CodeInfo is data for the uploaded contract WASM code"""

    code_hash: bytes = betterproto.bytes_field(1)
    creator: bytes = betterproto.bytes_field(2)
    source: str = betterproto.string_field(3)
    builder: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class ContractCustomInfo(betterproto.Message):
    enclave_key: bytes = betterproto.bytes_field(1)
    label: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ContractInfo(betterproto.Message):
    """ContractInfo stores a WASM contract instance"""

    code_id: int = betterproto.uint64_field(1)
    creator: bytes = betterproto.bytes_field(2)
    label: str = betterproto.string_field(4)
    created: "AbsoluteTxPosition" = betterproto.message_field(5)
    """
    never show this in query results, just use for sorting (Note: when using
    json tag "-" amino refused to serialize it...)
    """

    ibc_port_id: str = betterproto.string_field(6)


@dataclass(eq=False, repr=False)
class AbsoluteTxPosition(betterproto.Message):
    """AbsoluteTxPosition can be used to sort contracts"""

    block_height: int = betterproto.int64_field(1)
    """BlockHeight is the block the contract was created at"""

    tx_index: int = betterproto.uint64_field(2)
    """
    TxIndex is a monotonic counter within the block (actual transaction index,
    or gas consumed)
    """


@dataclass(eq=False, repr=False)
class Model(betterproto.Message):
    """Model is a struct that holds a KV pair"""

    key: bytes = betterproto.bytes_field(1)
    """hex-encode key to read it better (this is often ascii)"""

    value: bytes = betterproto.bytes_field(2)
    """base64-encode raw value"""


@dataclass(eq=False, repr=False)
class QuerySecretContractRequest(betterproto.Message):
    contract_address: str = betterproto.string_field(1)
    """address is the bech32 human readable address of the contract"""

    query: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class QueryByLabelRequest(betterproto.Message):
    label: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryByContractAddressRequest(betterproto.Message):
    contract_address: str = betterproto.string_field(1)
    """address is the bech32 human readable address of the contract"""


@dataclass(eq=False, repr=False)
class QueryByCodeIdRequest(betterproto.Message):
    code_id: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class QuerySecretContractResponse(betterproto.Message):
    data: bytes = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class QueryContractInfoResponse(betterproto.Message):
    """
    QueryContractInfoResponse is the response type for the Query/ContractInfo
    RPC method
    """

    contract_address: str = betterproto.string_field(1)
    """
    contract_address is the bech32 human readable address of the contract
    """

    contract_info: "ContractInfo" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class ContractInfoWithAddress(betterproto.Message):
    """
    ContractInfoWithAddress adds the contract address to the ContractInfo
    representation
    """

    contract_address: str = betterproto.string_field(1)
    """
    contract_address is the bech32 human readable address of the contract
    """

    contract_info: "ContractInfo" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class QueryContractsByCodeIdResponse(betterproto.Message):
    contract_infos: List["ContractInfoWithAddress"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class CodeInfoResponse(betterproto.Message):
    code_id: int = betterproto.uint64_field(1)
    creator: str = betterproto.string_field(2)
    """creator is the bech32 human readable address of the contract"""

    code_hash: str = betterproto.string_field(3)
    source: str = betterproto.string_field(4)
    builder: str = betterproto.string_field(5)


@dataclass(eq=False, repr=False)
class QueryCodeResponse(betterproto.Message):
    code_info: "CodeInfoResponse" = betterproto.message_field(1)
    wasm: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class QueryCodesResponse(betterproto.Message):
    code_infos: List["CodeInfoResponse"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryContractAddressResponse(betterproto.Message):
    contract_address: str = betterproto.string_field(1)
    """address is the bech32 human readable address of the contract"""


@dataclass(eq=False, repr=False)
class QueryContractLabelResponse(betterproto.Message):
    label: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryCodeHashResponse(betterproto.Message):
    code_hash: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class DecryptedAnswer(betterproto.Message):
    """DecryptedAnswer is a struct that represents a decrypted tx-query"""

    type: str = betterproto.string_field(1)
    input: str = betterproto.string_field(2)
    output_data: str = betterproto.string_field(3)
    output_data_as_string: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class DecryptedAnswers(betterproto.Message):
    answers: List["DecryptedAnswer"] = betterproto.message_field(1)
    output_logs: List[
        "___cosmos_base_abci_v1_beta1__.StringEvent"
    ] = betterproto.message_field(2)
    output_error: str = betterproto.string_field(3)
    plaintext_error: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState - genesis state of x/wasm"""

    codes: List["Code"] = betterproto.message_field(2)
    """Params params = 1 [(gogoproto.nullable) = false];"""

    contracts: List["Contract"] = betterproto.message_field(3)
    sequences: List["Sequence"] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class Code(betterproto.Message):
    """Code struct encompasses CodeInfo and CodeBytes"""

    code_id: int = betterproto.uint64_field(1)
    code_info: "CodeInfo" = betterproto.message_field(2)
    code_bytes: bytes = betterproto.bytes_field(3)


@dataclass(eq=False, repr=False)
class Contract(betterproto.Message):
    """
    Contract struct encompasses ContractAddress, ContractInfo, and
    ContractState
    """

    contract_address: bytes = betterproto.bytes_field(1)
    contract_info: "ContractInfo" = betterproto.message_field(2)
    contract_state: List["Model"] = betterproto.message_field(3)
    contract_custom_info: "ContractCustomInfo" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class Sequence(betterproto.Message):
    """Sequence id and value of a counter"""

    id_key: bytes = betterproto.bytes_field(1)
    value: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class MsgStoreCode(betterproto.Message):
    sender: bytes = betterproto.bytes_field(1)
    """sender is the canonical address of the sender"""

    wasm_byte_code: bytes = betterproto.bytes_field(2)
    """WASMByteCode can be raw or gzip compressed"""

    source: str = betterproto.string_field(3)
    """
    Source is a valid absolute HTTPS URI to the contract's source code,
    optional
    """

    builder: str = betterproto.string_field(4)
    """Builder is a valid docker image name with tag, optional"""


@dataclass(eq=False, repr=False)
class MsgStoreCodeResponse(betterproto.Message):
    """MsgStoreCodeResponse returns store result data."""

    code_id: int = betterproto.uint64_field(1)
    """CodeID is the reference to the stored WASM code"""


@dataclass(eq=False, repr=False)
class MsgInstantiateContract(betterproto.Message):
    sender: bytes = betterproto.bytes_field(1)
    """sender is the canonical address of the sender"""

    callback_code_hash: str = betterproto.string_field(2)
    code_id: int = betterproto.uint64_field(3)
    label: str = betterproto.string_field(4)
    init_msg: bytes = betterproto.bytes_field(5)
    init_funds: List["___cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(6)
    callback_sig: bytes = betterproto.bytes_field(7)
    """
    used internally for encryption, should always be empty in a signed
    transaction
    """


@dataclass(eq=False, repr=False)
class MsgInstantiateContractResponse(betterproto.Message):
    """MsgInstantiateContractResponse return instantiation result data"""

    address: str = betterproto.string_field(1)
    """Address is the bech32 address of the new contract instance."""

    data: bytes = betterproto.bytes_field(2)
    """Data contains base64-encoded bytes to returned from the contract"""


@dataclass(eq=False, repr=False)
class MsgExecuteContract(betterproto.Message):
    sender: bytes = betterproto.bytes_field(1)
    """sender is the canonical address of the sender"""

    contract: bytes = betterproto.bytes_field(2)
    """contract is the canonical address of the contract"""

    msg: bytes = betterproto.bytes_field(3)
    callback_code_hash: str = betterproto.string_field(4)
    sent_funds: List["___cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(5)
    callback_sig: bytes = betterproto.bytes_field(6)
    """
    used internally for encryption, should always be empty in a signed
    transaction
    """


@dataclass(eq=False, repr=False)
class MsgExecuteContractResponse(betterproto.Message):
    """MsgExecuteContractResponse returns execution result data."""

    data: bytes = betterproto.bytes_field(1)
    """Data contains base64-encoded bytes to returned from the contract"""


class QueryStub(betterproto.ServiceStub):
    async def contract_info(
        self,
        query_by_contract_address_request: "QueryByContractAddressRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryContractInfoResponse":
        return await self._unary_unary(
            "/secret.compute.v1beta1.Query/ContractInfo",
            query_by_contract_address_request,
            QueryContractInfoResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def contracts_by_code_id(
        self,
        query_by_code_id_request: "QueryByCodeIdRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryContractsByCodeIdResponse":
        return await self._unary_unary(
            "/secret.compute.v1beta1.Query/ContractsByCodeId",
            query_by_code_id_request,
            QueryContractsByCodeIdResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def query_secret_contract(
        self,
        query_secret_contract_request: "QuerySecretContractRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QuerySecretContractResponse":
        return await self._unary_unary(
            "/secret.compute.v1beta1.Query/QuerySecretContract",
            query_secret_contract_request,
            QuerySecretContractResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def code(
        self,
        query_by_code_id_request: "QueryByCodeIdRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryCodeResponse":
        return await self._unary_unary(
            "/secret.compute.v1beta1.Query/Code",
            query_by_code_id_request,
            QueryCodeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def codes(
        self,
        betterproto_lib_google_protobuf_empty: "betterproto_lib_google_protobuf.Empty",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryCodesResponse":
        return await self._unary_unary(
            "/secret.compute.v1beta1.Query/Codes",
            betterproto_lib_google_protobuf_empty,
            QueryCodesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def code_hash_by_contract_address(
        self,
        query_by_contract_address_request: "QueryByContractAddressRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryCodeHashResponse":
        return await self._unary_unary(
            "/secret.compute.v1beta1.Query/CodeHashByContractAddress",
            query_by_contract_address_request,
            QueryCodeHashResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def code_hash_by_code_id(
        self,
        query_by_code_id_request: "QueryByCodeIdRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryCodeHashResponse":
        return await self._unary_unary(
            "/secret.compute.v1beta1.Query/CodeHashByCodeId",
            query_by_code_id_request,
            QueryCodeHashResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def label_by_address(
        self,
        query_by_contract_address_request: "QueryByContractAddressRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryContractLabelResponse":
        return await self._unary_unary(
            "/secret.compute.v1beta1.Query/LabelByAddress",
            query_by_contract_address_request,
            QueryContractLabelResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def address_by_label(
        self,
        query_by_label_request: "QueryByLabelRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryContractAddressResponse":
        return await self._unary_unary(
            "/secret.compute.v1beta1.Query/AddressByLabel",
            query_by_label_request,
            QueryContractAddressResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgStub(betterproto.ServiceStub):
    async def store_code(
        self,
        msg_store_code: "MsgStoreCode",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgStoreCodeResponse":
        return await self._unary_unary(
            "/secret.compute.v1beta1.Msg/StoreCode",
            msg_store_code,
            MsgStoreCodeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def instantiate_contract(
        self,
        msg_instantiate_contract: "MsgInstantiateContract",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgInstantiateContractResponse":
        return await self._unary_unary(
            "/secret.compute.v1beta1.Msg/InstantiateContract",
            msg_instantiate_contract,
            MsgInstantiateContractResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def execute_contract(
        self,
        msg_execute_contract: "MsgExecuteContract",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgExecuteContractResponse":
        return await self._unary_unary(
            "/secret.compute.v1beta1.Msg/ExecuteContract",
            msg_execute_contract,
            MsgExecuteContractResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def contract_info(
        self, query_by_contract_address_request: "QueryByContractAddressRequest"
    ) -> "QueryContractInfoResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def contracts_by_code_id(
        self, query_by_code_id_request: "QueryByCodeIdRequest"
    ) -> "QueryContractsByCodeIdResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def query_secret_contract(
        self, query_secret_contract_request: "QuerySecretContractRequest"
    ) -> "QuerySecretContractResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def code(
        self, query_by_code_id_request: "QueryByCodeIdRequest"
    ) -> "QueryCodeResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def codes(
        self,
        betterproto_lib_google_protobuf_empty: "betterproto_lib_google_protobuf.Empty",
    ) -> "QueryCodesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def code_hash_by_contract_address(
        self, query_by_contract_address_request: "QueryByContractAddressRequest"
    ) -> "QueryCodeHashResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def code_hash_by_code_id(
        self, query_by_code_id_request: "QueryByCodeIdRequest"
    ) -> "QueryCodeHashResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def label_by_address(
        self, query_by_contract_address_request: "QueryByContractAddressRequest"
    ) -> "QueryContractLabelResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def address_by_label(
        self, query_by_label_request: "QueryByLabelRequest"
    ) -> "QueryContractAddressResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_contract_info(
        self,
        stream: "grpclib.server.Stream[QueryByContractAddressRequest, QueryContractInfoResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.contract_info(request)
        await stream.send_message(response)

    async def __rpc_contracts_by_code_id(
        self,
        stream: "grpclib.server.Stream[QueryByCodeIdRequest, QueryContractsByCodeIdResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.contracts_by_code_id(request)
        await stream.send_message(response)

    async def __rpc_query_secret_contract(
        self,
        stream: "grpclib.server.Stream[QuerySecretContractRequest, QuerySecretContractResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.query_secret_contract(request)
        await stream.send_message(response)

    async def __rpc_code(
        self, stream: "grpclib.server.Stream[QueryByCodeIdRequest, QueryCodeResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.code(request)
        await stream.send_message(response)

    async def __rpc_codes(
        self,
        stream: "grpclib.server.Stream[betterproto_lib_google_protobuf.Empty, QueryCodesResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.codes(request)
        await stream.send_message(response)

    async def __rpc_code_hash_by_contract_address(
        self,
        stream: "grpclib.server.Stream[QueryByContractAddressRequest, QueryCodeHashResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.code_hash_by_contract_address(request)
        await stream.send_message(response)

    async def __rpc_code_hash_by_code_id(
        self,
        stream: "grpclib.server.Stream[QueryByCodeIdRequest, QueryCodeHashResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.code_hash_by_code_id(request)
        await stream.send_message(response)

    async def __rpc_label_by_address(
        self,
        stream: "grpclib.server.Stream[QueryByContractAddressRequest, QueryContractLabelResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.label_by_address(request)
        await stream.send_message(response)

    async def __rpc_address_by_label(
        self,
        stream: "grpclib.server.Stream[QueryByLabelRequest, QueryContractAddressResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.address_by_label(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/secret.compute.v1beta1.Query/ContractInfo": grpclib.const.Handler(
                self.__rpc_contract_info,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryByContractAddressRequest,
                QueryContractInfoResponse,
            ),
            "/secret.compute.v1beta1.Query/ContractsByCodeId": grpclib.const.Handler(
                self.__rpc_contracts_by_code_id,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryByCodeIdRequest,
                QueryContractsByCodeIdResponse,
            ),
            "/secret.compute.v1beta1.Query/QuerySecretContract": grpclib.const.Handler(
                self.__rpc_query_secret_contract,
                grpclib.const.Cardinality.UNARY_UNARY,
                QuerySecretContractRequest,
                QuerySecretContractResponse,
            ),
            "/secret.compute.v1beta1.Query/Code": grpclib.const.Handler(
                self.__rpc_code,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryByCodeIdRequest,
                QueryCodeResponse,
            ),
            "/secret.compute.v1beta1.Query/Codes": grpclib.const.Handler(
                self.__rpc_codes,
                grpclib.const.Cardinality.UNARY_UNARY,
                betterproto_lib_google_protobuf.Empty,
                QueryCodesResponse,
            ),
            "/secret.compute.v1beta1.Query/CodeHashByContractAddress": grpclib.const.Handler(
                self.__rpc_code_hash_by_contract_address,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryByContractAddressRequest,
                QueryCodeHashResponse,
            ),
            "/secret.compute.v1beta1.Query/CodeHashByCodeId": grpclib.const.Handler(
                self.__rpc_code_hash_by_code_id,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryByCodeIdRequest,
                QueryCodeHashResponse,
            ),
            "/secret.compute.v1beta1.Query/LabelByAddress": grpclib.const.Handler(
                self.__rpc_label_by_address,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryByContractAddressRequest,
                QueryContractLabelResponse,
            ),
            "/secret.compute.v1beta1.Query/AddressByLabel": grpclib.const.Handler(
                self.__rpc_address_by_label,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryByLabelRequest,
                QueryContractAddressResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def store_code(
        self, msg_store_code: "MsgStoreCode"
    ) -> "MsgStoreCodeResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def instantiate_contract(
        self, msg_instantiate_contract: "MsgInstantiateContract"
    ) -> "MsgInstantiateContractResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def execute_contract(
        self, msg_execute_contract: "MsgExecuteContract"
    ) -> "MsgExecuteContractResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_store_code(
        self, stream: "grpclib.server.Stream[MsgStoreCode, MsgStoreCodeResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.store_code(request)
        await stream.send_message(response)

    async def __rpc_instantiate_contract(
        self,
        stream: "grpclib.server.Stream[MsgInstantiateContract, MsgInstantiateContractResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.instantiate_contract(request)
        await stream.send_message(response)

    async def __rpc_execute_contract(
        self,
        stream: "grpclib.server.Stream[MsgExecuteContract, MsgExecuteContractResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.execute_contract(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/secret.compute.v1beta1.Msg/StoreCode": grpclib.const.Handler(
                self.__rpc_store_code,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgStoreCode,
                MsgStoreCodeResponse,
            ),
            "/secret.compute.v1beta1.Msg/InstantiateContract": grpclib.const.Handler(
                self.__rpc_instantiate_contract,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgInstantiateContract,
                MsgInstantiateContractResponse,
            ),
            "/secret.compute.v1beta1.Msg/ExecuteContract": grpclib.const.Handler(
                self.__rpc_execute_contract,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgExecuteContract,
                MsgExecuteContractResponse,
            ),
        }
