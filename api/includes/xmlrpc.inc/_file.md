# includes/xmlrpc.inc

- **Source:** [local](../../../source/includes/xmlrpc.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpc.inc) · 659 lines

## File documentation

```text
@file
Drupal XML-RPC library.

Based on the IXR - The Incutio XML-RPC Library - (c) Incutio Ltd 2002-2005
Version 1.7 (beta) - Simon Willison, 23rd May 2005
Site:   http://scripts.incutio.com/xmlrpc/
Manual: http://scripts.incutio.com/xmlrpc/manual.php
This version is made available under the GNU GPL License
```

## Functions (derived index)

- [xmlrpc_value()](xmlrpc_value.md) — Turns a data structure into objects with 'data' and 'type' attributes.
- [xmlrpc_value_calculate_type()](xmlrpc_value_calculate_type.md) — Maps a PHP type to an XML-RPC type.
- [xmlrpc_value_get_xml()](xmlrpc_value_get_xml.md) — Generates XML representing the given value.
- [xmlrpc_message()](xmlrpc_message.md) — Constructs an object representing an XML-RPC message.
- [xmlrpc_message_parse()](xmlrpc_message_parse.md) — Parses an XML-RPC message.
- [xmlrpc_message_set()](xmlrpc_message_set.md) — Stores a copy of the most recent XML-RPC message object temporarily.
- [xmlrpc_message_get()](xmlrpc_message_get.md) — Returns the most recently stored XML-RPC message object.
- [xmlrpc_message_tag_open()](xmlrpc_message_tag_open.md) — Handles opening tags for XML parsing in xmlrpc_message_parse().
- [xmlrpc_message_cdata()](xmlrpc_message_cdata.md) — Handles character data for XML parsing in xmlrpc_message_parse().
- [xmlrpc_message_tag_close()](xmlrpc_message_tag_close.md) — Handles closing tags for XML parsing in xmlrpc_message_parse().
- [xmlrpc_request()](xmlrpc_request.md) — Constructs an object representing an XML-RPC request.
- [xmlrpc_error()](xmlrpc_error.md) — Generates, temporarily saves, and returns an XML-RPC error object.
- [xmlrpc_error_get_xml()](xmlrpc_error_get_xml.md) — Converts an XML-RPC error object into XML.
- [xmlrpc_date()](xmlrpc_date.md) — Converts a PHP or ISO date/time to an XML-RPC object.
- [xmlrpc_date_get_xml()](xmlrpc_date_get_xml.md) — Converts an XML-RPC date-time object into XML.
- [xmlrpc_base64()](xmlrpc_base64.md) — Returns an XML-RPC base 64 object.
- [xmlrpc_base64_get_xml()](xmlrpc_base64_get_xml.md) — Converts an XML-RPC base 64 object into XML.
- [_xmlrpc()](_xmlrpc.md) — Performs one or more XML-RPC requests.
- [xmlrpc_errno()](xmlrpc_errno.md) — Returns the last XML-RPC client error number.
- [xmlrpc_error_msg()](xmlrpc_error_msg.md) — Returns the last XML-RPC client error message.
- [xmlrpc_clear_error()](xmlrpc_clear_error.md) — Clears any previously-saved errors.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
