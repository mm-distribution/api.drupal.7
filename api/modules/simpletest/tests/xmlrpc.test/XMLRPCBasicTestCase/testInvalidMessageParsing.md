# XMLRPCBasicTestCase::testInvalidMessageParsing()

- **Type:** Method
- **File:** [`modules/simpletest/tests/xmlrpc.test`](../_file.md), lines 57–80 · [local source](../../../../../../source/modules/simpletest/tests/xmlrpc.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc.test#L57-L80)
- **Class:** [XMLRPCBasicTestCase](../XMLRPCBasicTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function testInvalidMessageParsing()
```

## Documentation

```text
Ensure that XML-RPC correctly handles invalid messages when parsing.
```

## Code

```php
  protected function testInvalidMessageParsing() {
    $invalid_messages = array(
      array(
        'message' => xmlrpc_message(''),
        'assertion' => 'Empty message correctly rejected during parsing.',
      ),
      array(
        'message' => xmlrpc_message('<?xml version="1.0" encoding="ISO-8859-1"?>'),
        'assertion' => 'Empty message with XML declaration correctly rejected during parsing.',
      ),
      array(
        'message' => xmlrpc_message('<?xml version="1.0"?><params><param><value><string>value</string></value></param></params>'),
        'assertion' => 'Non-empty message without a valid message type is rejected during parsing.',
      ),
      array(
        'message' => xmlrpc_message('<methodResponse><params><param><value><string>value</string></value></param></methodResponse>'),
        'assertion' => 'Non-empty malformed message is rejected during parsing.',
      ),
    );

    foreach ($invalid_messages as $assertion) {
      $this->assertFalse(xmlrpc_message_parse($assertion['message']), $assertion['assertion']);
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc.test) · Licensed GPL-2.0-or-later (see LICENSE)._
