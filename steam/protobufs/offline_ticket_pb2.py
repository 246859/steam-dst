# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: offline_ticket.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='offline_ticket.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14offline_ticket.proto\"w\n\x0eOffline_Ticket\x12\x18\n\x10\x65ncrypted_ticket\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12\x0c\n\x04kdf1\x18\x03 \x01(\x05\x12\r\n\x05salt1\x18\x04 \x01(\x0c\x12\x0c\n\x04kdf2\x18\x05 \x01(\x05\x12\r\n\x05salt2\x18\x06 \x01(\x0c'
)




_OFFLINE_TICKET = _descriptor.Descriptor(
  name='Offline_Ticket',
  full_name='Offline_Ticket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='encrypted_ticket', full_name='Offline_Ticket.encrypted_ticket', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='Offline_Ticket.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kdf1', full_name='Offline_Ticket.kdf1', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='salt1', full_name='Offline_Ticket.salt1', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kdf2', full_name='Offline_Ticket.kdf2', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='salt2', full_name='Offline_Ticket.salt2', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=143,
)

DESCRIPTOR.message_types_by_name['Offline_Ticket'] = _OFFLINE_TICKET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Offline_Ticket = _reflection.GeneratedProtocolMessageType('Offline_Ticket', (_message.Message,), {
  'DESCRIPTOR' : _OFFLINE_TICKET,
  '__module__' : 'offline_ticket_pb2'
  # @@protoc_insertion_point(class_scope:Offline_Ticket)
  })
_sym_db.RegisterMessage(Offline_Ticket)


# @@protoc_insertion_point(module_scope)