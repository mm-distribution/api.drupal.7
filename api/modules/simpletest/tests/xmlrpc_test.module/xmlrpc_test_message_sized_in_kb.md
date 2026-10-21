# xmlrpc_test_message_sized_in_kb()

- **Type:** Function
- **File:** [`modules/simpletest/tests/xmlrpc_test.module`](_file.md), lines 96–111 · [local source](../../../../../source/modules/simpletest/tests/xmlrpc_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module#L96-L111)
- **Module/theme:** batch_test

## Signature

```php
function xmlrpc_test_message_sized_in_kb($size)
```

## Documentation

```text
Created a message of the desired size in KB.

@param $size
  Message size in KB.
@return array
  Generated message structure.
```

## Code

```php
function xmlrpc_test_message_sized_in_kb($size) {
  $message = array();

  $word = 'abcdefg';

  // Create a ~1KB sized struct.
  for ($i = 0 ; $i < 128; $i++) {
    $line['word_' . $i] = $word;
  }

  for ($i = 0; $i < $size; $i++) {
    $message['line_' . $i] = $line;
  }

  return $message;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
