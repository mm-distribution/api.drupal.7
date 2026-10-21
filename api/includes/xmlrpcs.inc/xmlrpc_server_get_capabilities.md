# xmlrpc_server_get_capabilities()

- **Type:** Function
- **File:** [`includes/xmlrpcs.inc`](_file.md), lines 327–346 · [local source](../../../source/includes/xmlrpcs.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc#L327-L346)

## Signature

```php
function xmlrpc_server_get_capabilities()
```

## Documentation

```text
Returns a list of the capabilities of this server.

XML-RPC method system.getCapabilities maps to this function.

@return array
  Array of server capabilities.

@see http://groups.yahoo.com/group/xml-rpc/message/2897
```

## Code

```php
function xmlrpc_server_get_capabilities() {
  return array(
    'xmlrpc' => array(
      'specUrl' => 'http://www.xmlrpc.com/spec',
      'specVersion' => 1,
    ),
    'faults_interop' => array(
      'specUrl' => 'http://xmlrpc-epi.sourceforge.net/specs/rfc.fault_codes.php',
      'specVersion' => 20010516,
    ),
    'system.multicall' => array(
      'specUrl' => 'http://www.xmlrpc.com/discuss/msgReader$1208',
      'specVersion' => 1,
    ),
    'introspection' => array(
      'specUrl' => 'http://scripts.incutio.com/xmlrpc/introspection.html',
      'specVersion' => 1,
    ),
  );
}
```

---
_Drupal 7.103 · [includes/xmlrpcs.inc](https://github.com/drupal/drupal/blob/7.103/includes/xmlrpcs.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
