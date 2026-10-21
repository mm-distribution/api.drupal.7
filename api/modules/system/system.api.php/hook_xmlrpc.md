# hook_xmlrpc()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2440–2449 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2440-L2449)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_xmlrpc()
```

## Documentation

```text
Register XML-RPC callbacks.

This hook lets a module register callback functions to be called when
particular XML-RPC methods are invoked by a client.

@return
  An array which maps XML-RPC methods to Drupal functions. Each array
  element is either a pair of method => function or an array with four
  entries:
  - The XML-RPC method name (for example, module.function).
  - The Drupal callback function (for example, module_function).
  - The method signature is an array of XML-RPC types. The first element
    of this array is the type of return value and then you should write a
    list of the types of the parameters. XML-RPC types are the following
    (See the types at http://www.xmlrpc.com/spec):
      - "boolean": 0 (false) or 1 (true).
      - "double": a floating point number (for example, -12.214).
      - "int": a integer number (for example,  -12).
      - "array": an array without keys (for example, array(1, 2, 3)).
      - "struct": an associative array or an object (for example,
         array('one' => 1, 'two' => 2)).
      - "date": when you return a date, then you may either return a
         timestamp (time(), mktime() etc.) or an ISO8601 timestamp. When
         date is specified as an input parameter, then you get an object,
         which is described in the function xmlrpc_date
      - "base64": a string containing binary data, automatically
         encoded/decoded automatically.
      - "string": anything else, typically a string.
  - A descriptive help string, enclosed in a t() function for translation
    purposes.
  Both forms are shown in the example.
```

## Code

```php
function hook_xmlrpc() {
  return array(
    'drupal.login' => 'drupal_login',
    array(
      'drupal.site.ping',
      'drupal_directory_ping',
      array('boolean', 'string', 'string', 'string', 'string', 'string'),
      t('Handling ping request'))
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_xmlrpc()".

- [xmlrpc_test_xmlrpc()](../../simpletest/tests/xmlrpc_test.module/xmlrpc_test_xmlrpc.md) — `modules/simpletest/tests/xmlrpc_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
