import string
from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from random import choices, randint
from uuid import UUID, uuid4

payment_method_ids = [
    "2f30bd3c-e2a2-499d-ba5d-c093d85b8372",
    "dd76ebf6-7e64-4e7e-9040-f40d9b95ebcf",
    "d4def230-ea77-4d0d-8529-aef8a8ef0918",
    "5baa3e09-8ba6-45fd-ad22-810af4a81e2a",
    "4601d588-a7f0-4d59-9259-85432b4acb55",
    "61c2fca8-b0cd-4491-a11f-5d49c091a3db",
]

products_ids = [
    ("7d316f6b-ff20-41e4-a334-d03e1fd97c5e", 699),
    ("7d001b71-8635-44d4-8e43-d93289474a00", 3299),
    ("f1c211c1-930a-4753-bb75-6e8b06acc2b5", 1699),
    ("559a8a1f-85f9-4413-a51e-520bd97beaf6", 1665),
    ("bea59f62-387b-4840-b9cc-d6453a3746bf", 699),
    ("511a2641-63d1-436c-beed-c755a42f7fbe", 1379),
    ("f3790353-4f3b-43eb-8972-0c38957db350", 1049),
    ("6aeb3889-bb33-4949-a1eb-2d96c84ffe6c", 349),
    ("a48e809f-e37b-465c-b517-8794df64e877", 1699),
    ("3e1236f0-9464-48c2-beb4-fa9bd6c9857c", 1049),
    ("ce7de474-3692-47f3-83ce-640cc7a5c690", 3849),
    ("f215bb7e-7f63-41bd-9167-67d87be98a1e", 1049),
    ("63a18da3-241f-4756-b027-b18542c8e41c", 2049),
    ("3373dbc1-2b13-4eeb-bb4f-5bbea58c7d00", 1699),
    ("e8276afd-53fa-4c98-b92a-a4030f1859d2", 2350),
    ("59b73c5e-3a74-4d43-a053-41d79da5044e", 1049),
    ("fc34b389-077a-4e5d-85a8-d2db6d59b8de", 1699),
    ("7d98c51f-e8e7-4da7-ac03-c404987cd5a3", 699),
    ("e803f790-1df7-43b6-8693-5d5c4ac7b578", 1379),
    ("c3c0cfec-97b2-401c-b418-6465a3cf50ef", 349),
    ("b5803553-db63-45cb-9f5b-5f7e8f0af80e", 349),
    ("84a6ce6d-bb41-44b5-bba8-db9f630ce30b", 2350),
    ("d8e2052b-36f6-4089-b7f7-ee161914901c", 3299),
    ("55908d3b-5083-4410-bd88-b85eac14f7e4", 2649),
    ("3ca92559-b152-4890-bea3-ea4477a5aa6b", 999),
    ("2b8a7f48-946e-4392-8e58-cc4c4aae23db", 409),
    ("d0626583-a0eb-418a-ac84-547e6c49bc5e", 4699),
    ("08673d7b-d79f-40cb-bdac-f1a32386f21b", 349),
    ("b4637d5b-74fb-4152-b999-046773afea46", 32990),
    ("6c5a9f45-d17b-4e7a-afdc-b2b2ebcbad23", 1049),
    ("1a8b595d-68ca-4f7e-89cd-6546982c17c6", 699),
    ("31b48c93-212f-4f3c-a414-cff1865f7fec", 4237),
    ("ffbd834b-35b7-4371-8190-225629786b0b", 1379),
    ("dcd4bb2a-9d12-4479-9dbf-daaffc2a6985", 1699),
    ("f69a7b05-8acb-4abd-aa9f-50405d41018f", 2649),
    ("f0f75b4a-0d05-4b48-b62f-c72ec9c4b9e6", 2049),
    ("070baef9-8a3a-45fc-bee8-f6bd532b54ed", 53999),
    ("b500244f-8a3b-4596-beb2-9f525c4e2040", 53999),
    ("ccdd5013-bd30-4a51-a592-741d96753bdf", 1699),
    ("d7d7df27-6941-49fb-8664-b94a834c9e08", 1854),
    ("aca08be1-0b50-4f40-a3b1-4ea46d83ccfd", 349),
    ("bbeac95f-cee6-4558-9f65-253b6bf4cc22", 699),
    ("0c1ba007-278d-4884-b088-366dc9d2212f", 4699),
    ("247d2cac-0686-4aa3-aa8a-9063c73bc5b6", 5999),
    ("9dad8dd2-0792-4c6a-8c12-734d804ee4b7", 2350),
    ("bee9319f-b326-4dab-b56a-4d097a770059", 3299),
    ("d4ce1fd0-4121-425e-bd02-2ec982c25860", 1379),
    ("627d29b3-c53e-4ef2-aa96-5a14c84bce3a", 1049),
    ("931cc437-0b1a-40a3-8bbd-7c571d2b0cbd", 5999),
    ("20165d4e-130a-4567-8542-74c1d7ce231e", 2049),
    ("deae2749-cf8c-4115-89b1-d94ede10f6fe", 1844),
    ("f5a822c1-9b26-48ec-9834-58bd02179290", 349),
    ("6142895d-dec5-4e24-8df7-13d54e738d01", 2350),
    ("799178ae-cf2c-4d7e-a029-b56a00af0237", 4449),
    ("8bdb8ed9-4629-4a21-affb-51fe5b1c3cc9", 349),
    ("7859349a-0e33-47e4-8900-346bf379ef63", 2999),
    ("0345741a-7791-4b77-9824-90e5948dd9c7", 1699),
    ("56945020-f0d7-4f2f-8ce1-58eb842b89c1", 3299),
    ("cbdf4a5d-3201-4829-8880-ff766cf6039b", 1379),
    ("b36c4b0b-e62d-48e4-9e68-75d7e968141f", 1049),
    ("8c638acc-4fd5-4060-ba6b-9dc9966c0ef7", 1000),
    ("457865c8-61a6-443d-b991-b3b1d57cdf33", 3999),
    ("380d3585-1353-49b9-b9d6-b55e9298de60", 349),
    ("590b713e-eb85-49c1-910e-de0883f2a40f", 3849),
    ("d5ffc9ff-d08f-4b42-88e8-283c84a270e9", 500),
    ("1897ab6f-78ba-4806-840a-4864efd2a9f6", 2349),
    ("d275cc95-5ff8-47db-a488-b867550fe599", 1599),
    ("b82841f3-922d-4f7f-b7e0-30eb6438bcb4", 699),
    ("a046584b-a466-4068-a661-8e1225a5b658", 629),
    ("7c79c4a2-4a89-4ec0-b121-8554d959355e", 1379),
    ("ea0d6bb2-c9c9-4662-92a9-2d95bce33efc", 2049),
    ("4800c9c1-de93-42ce-8b03-4d788e8526f5", 1699),
    ("afece65e-03d7-4f39-b0a4-b00f21e5da9c", 2049),
    ("2b56b472-8c3e-4467-9a8d-df455e5f4350", 2999),
    ("682d9535-5373-43cc-be53-3dc4de849364", 2999),
    ("3f252bcc-c407-40eb-b6ee-fc2909165494", 2999),
    ("08806d17-2101-4b57-a376-037d73ae423d", 699),
    ("d23ff6f6-3cb0-42c5-88d0-9c4b3c84fd0a", 599),
    ("54d6fe47-21d6-4426-8060-ed5a7a8873a7", 349),
    ("4dc76a89-9c84-49e0-b52a-a52f3140b73d", 1049),
    ("1705ee07-0509-418e-828d-e95f346e7caa", 4449),
    ("f5c5a04f-bb44-4c65-ba37-198a3d7e63c4", 699),
    ("3c94a05c-dc16-4a12-8395-c2d213bd3ec8", 349),
    ("34050ace-ff91-4e2e-8084-087f4d44dd83", 594),
    ("5e3e06c6-a062-4138-b7c9-377420d3e10c", 209),
    ("786cbe8e-b688-488e-8c0d-d6d744746172", 1379),
    ("27700151-8cd0-4f9c-b3c3-50a708464fb7", 2018),
    ("27aa7e8c-23dc-430f-97c9-44b560649799", 2649),
    ("e85aa06e-5709-4821-a576-da00281fd394", 2649),
    ("3364ab6c-78c2-48fa-9497-76db26115533", 279),
    ("dd9e9847-427e-4ebd-a5dc-a33fe01c135f", 699),
    ("182350f3-4639-4202-8d30-7e7c29d05e05", 699),
    ("5ee3e1eb-b8ae-47ab-af25-fa54183d333e", 2649),
    ("da0e641e-6513-43e3-b9ea-32cbc9c1345c", 1699),
    ("d75d7943-eabf-4ddf-a105-f22c94b599b7", 7399),
    ("9162146a-7cc2-4d8f-a4c7-999b5266269f", 699),
    ("8545e6fe-af27-4d2e-bbee-9f131df45c4a", 499),
    ("e87173ec-8fe8-4807-87d4-c13d42c73283", 3579),
    ("bd40d06b-1600-43f4-9e76-58d797cc6427", 4449),
    ("868c60b4-02c4-44f6-82ce-7c38fc195dc6", 1299),
    ("0c0d843e-52c6-440a-834c-20fe1d92ac85", 2049),
    ("16b37fef-ff9d-4044-b8cb-6230c5645b27", 1099),
    ("189c598b-3c5d-484b-8b3d-f83c78e06773", 1399),
    ("60a1f1f5-f7eb-4b35-8a00-5111427a0f99", 1299),
    ("a0af216d-7f24-43e3-99ad-748dd556d5bc", 349),
    ("1cb0f7eb-d33e-4af6-8c5b-7260568a7981", 1379),
    ("f468c6d0-488d-4770-9f12-117ccf2ac730", 54795),
    ("6efcbcef-1297-4aa2-806c-205854cc4f3b", 1499),
    ("7db3d61c-432f-42ff-8fdf-8c8ad160e106", 629),
    ("fe5a15be-03b5-4076-81b0-c05cf6ed1a0f", 3579),
    ("ebad7ed8-1702-4ab5-8e31-6c20418f8207", 1986),
    ("b07144e8-7a8c-416a-a47a-f093101ea57e", 1049),
    ("2af4a047-8dbb-4a05-b65d-a4e7de77feb1", 1049),
    ("a71ec5a4-db25-4241-989f-e818ae8e9190", 1049),
    ("bf03e8f2-3f60-4230-8c4c-12a17bda4902", 2350),
    ("236eca84-2187-4cc1-acf2-e250bcbab122", 524),
    ("f9cba0a6-9571-46ad-b57d-30fed8ca6bce", 2999),
    ("36cab74a-5e1c-47bd-8831-cc818142e3a7", 500),
    ("1590ae6b-e812-441f-9716-640e5f181726", 1150),
    ("ca64b288-407b-4e4b-bf66-76e815f5887c", 4599),
    ("e05555b6-940d-4086-96d4-bb3890ea68f6", 99),
    ("2593aa44-8e2d-4466-8ef4-2261a1bdab42", 3299),
    ("773faae4-3577-410a-bc9a-050d94271899", 2320),
    ("2239287b-690a-4971-8e2c-625c3e0a358f", 1189),
    ("d312cb0b-c42f-4d4e-b00c-b8ca60d3ebd2", 2049),
    ("7a5b522c-ccec-43d3-8546-beefad043b5b", 1379),
    ("b479202d-405a-4e6c-b5e7-ba59531cd31d", 2649),
    ("2b5a3464-9d74-40cd-9685-238d90ba3d87", 4699),
    ("5359719d-330c-4e71-b925-beae0bfc8ba7", 4699),
    ("80df5b85-f6b8-4b53-b316-3a59a8411705", 7399),
    ("90f0cec1-2b88-4d3e-a6fb-a457ac1c7670", 7399),
    ("61bf5cb0-ac03-4bc4-bf7f-d62eb9ce2bd7", 7399),
    ("d59261a2-9730-46db-8999-4723e2d1f030", 5999),
    ("42fe0dd3-5db1-4ba9-a559-0347ae0ce619", 7399),
    ("d338557c-6371-4764-9493-cc49907e808c", 5999),
    ("7af32fb3-3454-419f-ba78-82d82e8500bd", 3299),
    ("92f8485f-bec5-4416-b765-a2913a4249fa", 349),
    ("0d51c5e0-fa83-4d15-a567-d9b5e0151c2b", 1699),
    ("71cb7e3a-3ec6-48ab-a9ad-ca3ff144038d", 1049),
    ("078c6c96-5b6d-4293-b614-0de6cf1d66dc", 699),
    ("e8299301-ca81-4912-a8cc-ef38e8824c0e", 629),
    ("ac51819c-1435-4a16-8511-cec5b446d5d8", 699),
    ("74618617-04be-47bc-b501-fb447321ee6a", 1699),
    ("a3e9a289-f9a0-48fe-8bbd-f00e95bfb49d", 1499),
    ("18d480fa-37d1-449f-9026-7ecee2cf06ba", 1379),
    ("8bdb8720-2ce4-4d7e-a1c4-f2ead4d2b456", 2321),
    ("70db1ad6-3e1b-4fbd-8d78-3550399c46c3", 349),
    ("a212cff8-7444-444f-b107-61e07623b9c1", 299),
    ("c729f572-3b44-432e-a9c9-82707d2b8b3f", 349),
    ("a8d06048-c727-43be-8211-001c1e5e07c9", 1049),
    ("c629cad4-878c-4977-8374-97e2dc177066", 349),
    ("de4c2054-654a-4999-924f-43fc558c1345", 1379),
    ("1b739c34-1aab-4f67-9a50-7adbca910968", 349),
    ("41777b2c-acb5-493e-a5ab-685bef281bfc", 2350),
    ("842f541d-f09c-4c1e-a680-f1112a696c85", 2499),
    ("f20ffc6c-4a8e-44d4-9a56-fc715133850c", 1699),
    ("2bf3d3d5-99a4-49cd-adf2-70835d316fae", 2636),
    ("102ecfc3-1a74-4aca-ad5e-9d563cfca334", 349),
    ("e00a57b6-8284-414d-a9e2-f9313b761b72", 349),
    ("f6424ca4-caf4-4449-9d41-ba366cd90f61", 1379),
    ("253dc2a9-5415-4c17-8897-01c1897079e2", 1379),
    ("3addffb9-40bc-4f85-bc15-34ef37c44e5d", 1699),
    ("8a10645c-d9fa-46cb-8cdc-6012eea8dca9", 1319),
    ("5e68c8bc-a8ee-4d78-aab4-d75aa3b3a512", 1319),
    ("c9015a21-d433-498d-9340-a98a46eed218", 2999),
    ("f85ad729-2cec-452c-a1cb-18dd06a510f8", 1799),
    ("459190e6-0be6-4f02-a642-c3bff6502611", 499),
    ("e79322a2-5df1-4e79-8708-144a0842619e", 349),
    ("87137584-e7de-4c03-8b13-1ff2eb23904d", 3299),
    ("1d2112a2-03a4-489e-b72b-78b1dbc851c2", 1049),
    ("23860fc4-567b-4061-b941-5713aa75cd17", 1699),
    ("c26cc486-b572-40cd-9f13-9d2731c18b84", 349),
    ("f2954a60-a226-446c-8838-4c0bbf290a11", 1699),
    ("158a6cf9-9bfc-4908-9aa8-d4d9102e93df", 2649),
    ("f0500a09-be36-473f-ab81-dfdeb989b78a", 349),
    ("4a591415-3a82-4e72-8b76-d97da8b879a3", 2049),
    ("fa50e692-e79b-47fa-963b-b4ce455e5776", 99),
    ("820f54b6-daaf-422e-9d60-dab5e9282536", 349),
    ("71022322-df67-419f-9c58-29089a6cdb9b", 1049),
    ("bdaf0649-1f9c-4ba7-93e7-562875161042", 3299),
    ("b6dbec59-cdc2-4a67-9bb2-9ae10924cdb4", 1699),
    ("3e8b3caa-9f78-446e-8dcc-e8f21cdf20b3", 2999),
    ("789ae3f9-d757-4b31-aca7-569229cd2500", 3299),
    ("d8f867ff-542e-46ac-9e64-051766653a2d", 2350),
    ("f11b04c8-a735-4a42-a418-c70301afed6c", 699),
    ("4628f44a-122f-4986-b104-18575acf9887", 699),
    ("460b1b43-f28d-4203-a65b-c25f302f8fae", 699),
    ("ca982d8b-fb11-4ee1-8a60-2c7b30d28296", 2350),
    ("b7417058-f21c-4c62-a810-5c03174f7ef9", 1440),
    ("e12a1095-de16-4638-8926-6541c6fd2a9a", 4699),
    ("d644d020-78a2-4584-8d8b-fc85457455db", 349),
    ("de0251b5-b874-4e7b-bfa9-d3834471fe3d", 299),
    ("39c03f4d-cff4-4c9d-b42e-e3b027560247", 1699),
    ("b5266b9a-9109-42e7-9a84-4bb4fcb0d767", 699),
    ("37d9230a-0551-4def-9f4f-63bdf9f37c5f", 3299),
    ("b4cdf643-59c5-4649-a150-d81fc2f02bc4", 699),
    ("812fb165-fb78-40a0-86c6-a192d723e542", 2049),
    ("61da0f21-00eb-4e71-abec-c6fc5b627750", 1379),
    ("97c733d9-9849-49be-bff5-31419f20baaa", 1049),
    ("92bd1006-3eed-4d4d-aba9-0f366c3b625f", 1049),
    ("1b49d456-8db0-48be-a4af-10e8638b8094", 1049),
    ("089dffba-81cc-43e9-9981-ec347dbe8999", 10795),
    ("cdcb1893-4385-43fc-bbfa-223a3c0171e0", 1699),
    ("2184ee3a-6ace-4ea9-8a3e-c194249e8209", 5999),
    ("cd3162d2-8114-4adb-af3b-400109d6a9b8", 1327),
    ("2cce5151-c6ab-4f4a-a690-70cd94e5b515", 2649),
    ("319a02e6-c666-432b-a649-f29ad1660e4c", 349),
    ("9e124a24-b9a9-4e81-a749-f89a2a95bfd3", 2000),
    ("59e59496-5f1f-49f4-a314-400cfd9701bf", 809),
    ("27edbd47-1e16-4c86-abdb-472de379fd28", 2049),
    ("6d48e96e-3054-4614-a0b0-8822b489bca4", 2649),
    ("251dc1bf-c41d-402e-ba86-7cbd9b30dbd0", 1049),
    ("9e5d9798-80be-40c2-948c-f129dfd8b053", 1699),
    ("3efc2267-bce7-4b5d-bdcc-50540ecd0afd", 1999),
    ("4d46ee6f-69a2-43e3-967b-923926ddd2d7", 2049),
    ("290281ea-ef49-423d-ae82-5f93553a08d2", 2649),
    ("f04a0961-f2d7-4b26-8eda-4d9b5cc7495d", 699),
    ("ff77a147-f0dd-4ac3-b8ea-ae0b9f7deed1", 3000),
    ("c74428de-9139-4b8b-b2f0-32888e5166fa", 349),
    ("88e816c1-37f5-4dd5-8b17-51e3442195bf", 349),
    ("1d87404b-ce78-4bea-8b0f-41d86360bb1a", 2115),
    ("fd03f219-e805-413a-9ad4-c8a0d98a7447", 349),
    ("a1ca95ae-7c7f-4d3b-891d-7eebc3dfa57c", 1699),
    ("61fc0abd-885b-4300-b9d4-d11fe573672a", 3849),
    ("c1a1e00b-e967-4e41-85cf-3c190a2be44c", 1049),
    ("514273e9-842e-4e8d-998a-49f5e2a1c14a", 1699),
    ("46fd66a2-ac36-4ea4-a3df-e0a6a13fb0dd", 1699),
    ("482eadbd-5281-489e-8616-41b5b563d40c", 4199),
    ("c001d878-30d1-4fbb-a406-cac2e54b1635", 1049),
    ("e94bc803-7e6f-4598-b13c-b6e71a4bbf6c", 1699),
    ("328ba0af-61d6-4538-9c5a-44912db1095d", 10199),
    ("ac4765fd-3587-4976-a36a-b9911d5f3406", 1854),
    ("b6c3aa5a-0291-4997-8122-bd2f247f5927", 1379),
    ("9bff8833-ff89-4d75-b68d-51e7b4f34cbf", 1049),
    ("90ba93c5-e06b-405d-b306-355c7e31a238", 749),
    ("ea375096-5cb3-49f7-b8d1-dc10e8d7cb83", 499),
    ("a9d0edfc-2e9d-48fc-b5f1-722240a06769", 499),
    ("a010b280-fa6a-420d-966b-a24d6d2eddfe", 399),
    ("499dc5f2-24f4-4989-af23-288e8ffe1c0e", 199),
    ("71be5c98-7dd6-49e2-8c05-e24e7bc80a08", 999),
    ("5d054fff-03e8-4234-9475-37518ba65268", 499),
    ("22bbb95e-6bae-49ee-84a7-2d4a4bbd8a75", 1679),
    ("bece2c8c-ab77-4c2b-8f53-7f5eaad18f19", 2599),
    ("1c6b707f-e08e-47a9-8564-7642c332e1dc", 2999),
    ("be64a5bb-8c5f-4e3a-a705-fe3c6bdc3ed3", 1499),
    ("029b0b23-7591-41c3-a934-ce4b56a87d8f", 4999),
    ("bc82ca67-403f-4e58-93e0-de8090447990", 1379),
    ("39734b5a-834e-4d10-b2f6-ee67b0ee6e20", 699),
    ("a14347c0-b9c8-4715-b375-1092941c3960", 4699),
    ("a108e12a-4056-4d18-9373-a031e89c92f9", 1000),
    ("572ea740-3da2-47cf-98f9-b516c701b955", 1049),
    ("ce1cec42-4cf7-480e-b56d-8dbf423fbd0c", 1049),
    ("dc61c3c2-3ce3-4eee-9491-e2b81a1b2dfc", 1049),
    ("9b8e4ba1-1cbf-49c8-b4a4-a1bac445df4a", 699),
    ("ec12a162-bdf1-4b87-b735-0bc3af0ee260", 699),
    ("97508b57-19d0-40d3-81ca-183d399d9891", 699),
    ("b132bcec-db0a-4aa4-87ca-67cf4bcdf05a", 699),
    ("f3226cd7-bc92-450b-820a-4c076365618e", 1359),
    ("2da15ad8-41a0-4520-8e35-2babab13ef0e", 1049),
    ("3a6b5c08-f636-4220-bd85-106a3d68250d", 1699),
    ("de152bae-56de-490a-b88d-ee674a765056", 1049),
    ("d61fb375-5718-4be4-89a2-1726317aca31", 1699),
    ("84d40147-90e2-469b-8d71-eca602e033e3", 1331),
    ("475215b6-37f4-4549-b2d9-5a148fc4013c", 2649),
    ("752d2534-4b30-4363-bc9c-7ddf4908ff62", 2999),
    ("c6fee735-e9d8-4b82-8564-1d09b86111b0", 5499),
    ("655604b0-b175-41bf-9452-51f388605c96", 2999),
    ("13927038-a637-4230-af0e-041cefa3b3a3", 2999),
    ("9f3da1eb-8ff1-4f2a-8082-3c9a55b8e169", 5499),
    ("00d67fe2-db44-40d3-9eae-b850d97f5a18", 2999),
    ("5cb1887e-aa38-4d62-aa56-3ca84c9d5cee", 349),
    ("b451e36c-39bd-4878-91a0-8260a074def4", 299),
]

user_ids = [
    "5483cb1e-473f-4fc2-9e50-524e67a00f28",
    "7ccd6e68-554f-4522-8dc0-ad4e71d0aadf",
    "5eb5d6fd-e923-4b0d-84f3-3c678a31308d",
    "d671153f-3571-4ab2-a130-74e2eb403ec4",
    "f136b401-0619-4328-88c1-36adc91c4de1",
    "9feb20cd-d915-4b65-bcfc-3f1931be5853",
    "d022e8ee-f2f1-4065-b625-25ba3954cabd",
    "7e622661-bb32-4d9f-b889-b508b59af0eb",
    "0c36b391-c1b4-42a0-855b-8720e72af9fd",
    "5f80ba3c-cdd1-4ab2-8360-b5cb56f564a4",
    "06300e5f-e629-422b-a52b-d651178634e3",
    "208e1dd6-6260-4ef3-8e86-8aae7f2ebf19",
    "d5bdca66-90c5-40bf-baeb-df9317290666",
    "c1fda49c-4644-47a1-a03f-98a7052ceebf",
    "5d9baab0-75e5-4828-8840-4a6d15336a73",
    "09d7e2de-9325-43c9-97b0-744da393ce3f",
    "e624217a-be7e-415f-a04f-902405381288",
    "f24d5ab5-c258-403e-8bf3-32e4f58d0d35",
    "b8355472-56b6-4dcb-8c52-6b97806979fa",
    "4d1b2d1e-9ecd-4ed1-aeb1-9420a8b64e91",
    "a4907675-6e95-4e89-b77c-30d7685e019d",
    "5e283981-6cdb-43d0-b50e-e3013e08cba5",
    "614e5dd0-0dbc-445c-811b-c393816d7d8e",
    "1cbb57c0-0da7-4e5f-b227-984a231a2e75",
    "ed0b5531-5e1f-4b62-b295-7ec5f67ff3e4",
    "e7b45a52-4271-4797-8141-6e6a431fddb1",
    "cf615957-e113-44a8-aa79-740a06a42d1d",
    "ec2022f0-3897-46a0-835b-8d580eca5085",
    "8f600c1f-a1f1-4bd8-af02-40eed8ddde4b",
    "f2e1ddd7-218a-4432-9d7d-48c94aeba20d",
    "2477e7bc-a388-4ade-bbdd-6f35832b511c",
    "d39aecfa-645c-485d-bb3d-79f2470503ab",
    "4a682f75-7216-47a0-8dc2-e42726de04b9",
    "2b898965-5ebd-4455-ab60-358e78dc9145",
    "b12e17f9-bf27-4dca-95f1-d1a8176eb198",
    "6f21276b-3d98-40e8-9137-25f3933c4068",
    "ba2ed024-b626-4570-99ac-79bd8edb3a96",
    "4f25634e-148e-4664-a1ae-4d7659e20235",
    "754de407-3eaa-4fd1-b8b2-8f3fd2f64137",
    "cefd24f0-2674-4fdb-9fd2-7e4ecf5b73ef",
    "782dcfc0-48be-455a-8688-56ddae4fd560",
    "470f6845-82a4-4f0b-b908-4144283cb2ec",
    "311e5578-362e-491f-b9a4-94ce07307d97",
    "25ae26f6-6f6d-4769-8d3b-a76d19593a06",
    "4c449d01-8008-4c97-b6a6-ed67485a1a61",
    "2323a099-60a3-4e4e-95c7-d303ac658b96",
    "0dac1044-0ba5-4aa1-aa19-03de18f433c6",
    "83259a66-e89b-4670-89a2-97f64d39bf03",
    "02e24c25-f061-4602-8e23-27c5be8a1060",
    "b89bbc29-e511-4de9-abe2-5289b276c07e",
    "c630ad44-ca0a-4164-afed-1e58d279689c",
    "2ef3818b-656e-4529-810c-5dd35379ba32",
    "e6deb3aa-d1cd-42b0-b7c9-b1fdfe1ad8b9",
    "50027829-fe04-470e-a7f9-a5aacdc4598d",
    "6fd6f168-dd0c-4043-aebf-588e04602aaa",
    "3cafd4c5-1ca1-4d68-937c-4d83722b8874",
    "00c703ce-8839-497a-ad9d-d050c930dfd6",
    "de6133eb-38e7-4157-bc7a-ac4300c6c71a",
    "7ce76b65-21bb-4992-81ff-d508f805513f",
    "26334f38-f67d-462b-ab11-a6dab333282b",
    "1f2a9e9c-1ac6-46b7-ac57-bf333c5264b4",
    "69f688f7-cc09-4924-a3b2-abe83ab44dd8",
    "d0d245ee-3fe1-4b7f-9675-64296a1c7c4c",
    "283b54e9-d274-4561-9fcf-281cc869d98b",
    "2d531b9f-2aec-4fa9-abac-5e1d03a9a309",
    "759a41b6-f003-4b4f-b244-71c44b7f6cd5",
    "c32e8260-8405-48cc-aa4f-468052f201e8",
    "655e72ee-27b0-4629-9e42-68ee571f1863",
    "c4583898-9270-4845-a772-8ce02c2cf5f6",
    "db7da093-f179-44b2-b6fb-1e1e668db65e",
    "1ba4460c-8a8a-450c-9b6c-d77f221a234a",
    "6d60eda9-0a18-4c78-9c0b-03166da4a48d",
    "76cc4aeb-9b56-4d68-b6ec-4f1f36d7fca6",
    "877ed13d-2717-446b-8efe-f4cf0b964ca2",
    "a7098080-6ecf-4de2-a767-5e5ee22f326f",
    "131ae462-7b67-48a0-a52f-63f2dacf9fb6",
    "79f17dc1-6cce-4d4f-a082-1590c69d9f29",
    "dcd8c123-c6cf-4fcf-8f37-2a6260528c05",
    "386215e9-b5b7-48e7-b62c-684b55be4dd2",
    "a927c034-12b8-406e-a03c-259d4553282d",
    "d7c5ea31-0f4c-4039-9589-0afa2baf0c6a",
    "f28e0bae-8f32-45a3-a695-682518dfa03d",
    "b77b1d5b-a0de-4d89-8cdd-e898c63e080f",
    "e232e82c-e8c3-46e3-ab03-4ef17d75d5e8",
    "e808d22c-a8b1-490b-ad7f-51f9dd00fc57",
    "0ed8fcb2-1919-4fa0-9647-21c00a846494",
    "49b0e812-c863-4a03-9ed5-58b5a515cbce",
    "30fde38e-040f-415d-9e37-6d164058a0d4",
    "1068140d-9202-4e18-acca-d4381415feac",
    "20ed1802-2476-499f-a0b2-d323a4591f05",
    "ce2947ef-1434-4ce4-8f2c-d2272090d8fb",
    "24458d7b-8c0f-4eb9-becb-697891a96458",
    "f90b2f2e-eb60-4eb5-8e0e-a162c3c00e22",
    "757464e7-da81-4501-b526-a503243a7c77",
    "a127aedb-e412-4074-8bab-474a7b941eaf",
    "79d6906a-98d3-441e-aeba-b0662fec0eca",
    "04df3b35-2fd9-4171-aa74-0aebe029c595",
    "4b5140ec-ebc6-4f74-9443-c5081f9ef320",
    "72fba527-78d6-4433-a2fb-cb42b44c09fc",
    "1f5621e6-90bb-46c7-8621-5f20f7f6bcba",
]


@dataclass
class Game:
    id: UUID
    title: str
    publisher: str
    parental_guidance: str
    release_date: date
    updated_at: datetime
    price: int
    genre: str
    system: str
    discount: int


class Status(Enum):
    New = "new"
    Pending = "pending"
    Cancelled = "cancelled"
    Paid = "paid"
    Sent = "sent"
    PartialSent = "partial_sent"


@dataclass
class Order:
    id: UUID
    code: str
    user_id: UUID
    payment_method_id: UUID
    status: Status
    coupon_code: str
    created_at: datetime
    updated_at: datetime


@dataclass
class OrderItem:
    id: UUID
    order_id: UUID
    product_id: UUID
    price: int
    discount: int


orders: list[Order] = []
order_items: list[OrderItem] = []
statuses = [s for s in Status]
for _ in range(500):
    user_id = choices(user_ids, k=1)[0]
    payment_method_id = choices(payment_method_ids, k=1)[0]
    prod_ids = choices(products_ids, k=randint(1, 5))
    code = "".join(choices(string.ascii_uppercase + string.digits, k=16))
    status = choices(statuses, k=1)[0]
    coupon_code = choices(["GAMEISLIFE", "10OFF", ""], k=1)[0]
    order = Order(
        id=uuid4(),
        code=code,
        user_id=UUID(user_id),
        payment_method_id=UUID(payment_method_id),
        status=status,
        coupon_code=coupon_code,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    orders.append(order)

    for product_id in prod_ids:
        discount = choices([0, 5, 1], k=1)[0]
        order_item = OrderItem(
            id=uuid4(),
            order_id=order.id,
            product_id=UUID(product_id[0]),
            price=product_id[1],
            discount=discount,
        )
        order_items.append(order_item)

with open("orders_insert.sql", "w") as sql_file:
    sql_file.write(
        "INSERT INTO orders (id, code, user_id, payment_method_id, status, coupon_code, created_at, updated_at) VALUES\n"
    )
    for order in orders:
        sql_file.write(
            f"('{order.id}', '{order.code}', '{order.user_id}', '{order.payment_method_id}', '{order.status.value}', '{order.coupon_code}', '{order.created_at.isoformat()}', '{order.updated_at.isoformat()}'),\n"
        )

with open("orders_items_insert.sql", "w") as sql_file:
    sql_file.write(
        "INSERT INTO orders_items (id, order_id, product_id, price, discount) VALUES\n"
    )
    for order_item in order_items:
        sql_file.write(
            f"('{order_item.id}', '{order_item.order_id}', '{order_item.product_id}', {order_item.price}, {order_item.discount}),\n"
        )
