# CommonXssUnitTest::testBadProtocolStripping()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 555–585 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L555-L585)
- **Class:** [CommonXssUnitTest](../CommonXssUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testBadProtocolStripping()
```

## Documentation

```text
Check that harmful protocols are stripped.
```

## Code

```php
  function testBadProtocolStripping() {
    // Ensure that check_url() strips out harmful protocols, and encodes for
    // HTML.
    $url = 'javascript:http://www.example.com/?x=1&y=2';
    $expected_html = 'http://www.example.com/?x=1&amp;y=2';
    $this->assertIdentical(check_url($url), $expected_html, 'check_url() filters a URL and encodes it for HTML.');

    // Ensure that drupal_strip_dangerous_protocols() can be used to return a
    // plain-text string stripped of harmful protocols.
    $data = array(
      'javascript:http://www.example.com/?x=1&y=2' => 'http://www.example.com/?x=1&y=2',
      'foo://disallowed.com' => '//disallowed.com',
      'http://example.com' => 'http://example.com',
      'https://example.com' => 'https://example.com',
      'www.example.com' => 'www.example.com',
      'mailto:person2@example.com' => 'mailto:person2@example.com',
      'person2@example.com' => 'person2@example.com',
      'ftp://example.com' => 'ftp://example.com',
      'sftp://secure.host' => 'sftp://secure.host',
      'ssh://odd.geek' => 'ssh://odd.geek',
      'news://example.net' => 'news://example.net',
      'telnet://example' => 'telnet://example',
      'irc://example.host' => 'irc://example.host',
      'webcal://calendar' => 'webcal://calendar',
      'rtsp://127.0.0.1' => 'rtsp://127.0.0.1',
      'tel:111111111' => 'tel:111111111',
    );
    foreach ($data as $url => $expected_plain) {
      $this->assertIdentical(drupal_strip_dangerous_protocols($url), $expected_plain, 'drupal_strip_dangerous_protocols() filters a URL and returns plain text.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
