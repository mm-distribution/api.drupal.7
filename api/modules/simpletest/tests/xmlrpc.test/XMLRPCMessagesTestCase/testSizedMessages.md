# XMLRPCMessagesTestCase::testSizedMessages()

- **Type:** Method
- **File:** [`modules/simpletest/tests/xmlrpc.test`](../_file.md), lines 213–227 · [local source](../../../../../../source/modules/simpletest/tests/xmlrpc.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc.test#L213-L227)
- **Class:** [XMLRPCMessagesTestCase](../XMLRPCMessagesTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSizedMessages()
```

## Documentation

```text
Make sure that XML-RPC can transfer large messages.
```

## Code

```php
  function testSizedMessages() {
    // These tests can produce up to 128 x 160 words in the XML-RPC message
    // (see xmlrpc_test_message_sized_in_kb()) with 4 tags used to represent
    // each. Set a large enough tag limit to allow this to be tested.
    variable_set('xmlrpc_message_maximum_tag_count', 100000);

    $xml_url = url(NULL, array('absolute' => TRUE)) . 'xmlrpc.php';
    $sizes = array(8, 80, 160);
    foreach ($sizes as $size) {
      $xml_message_l = xmlrpc_test_message_sized_in_kb($size);
      $xml_message_r = xmlrpc($xml_url, array('messages.messageSizedInKB' => array($size)));

      $this->assertEqual($xml_message_l, $xml_message_r, format_string('XML-RPC messages.messageSizedInKB of %s Kb size received', array('%s' => $size)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc.test) · Licensed GPL-2.0-or-later (see LICENSE)._
