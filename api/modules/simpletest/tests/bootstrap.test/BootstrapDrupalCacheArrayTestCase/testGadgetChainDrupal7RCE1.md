# BootstrapDrupalCacheArrayTestCase::testGadgetChainDrupal7RCE1()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 926–964 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L926-L964)
- **Class:** [BootstrapDrupalCacheArrayTestCase](../BootstrapDrupalCacheArrayTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testGadgetChainDrupal7RCE1()
```

## Documentation

```text
Simulate unsafe deserialization of payload prepared by the phpggc project.

@see https://github.com/ambionics/phpggc/pull/28
```

## Code

```php
  public function testGadgetChainDrupal7RCE1() {
    // phpggc -s Drupal7/RCE1 phpinfo 2
    $payload = 'O:11:"SchemaCache":4:{s:6:"%00*%00cid"%3Bs:14:"form_DrupalRCE"%3Bs:6:"%00*%00bin"%3Bs:10:"cache_form"%3Bs:16:"%00*%00keysToPersist"%3Ba:3:{s:8:"#form_id"%3Bb:1%3Bs:8:"#process"%3Bb:1%3Bs:9:"#attached"%3Bb:1%3B}s:10:"%00*%00storage"%3Ba:3:{s:8:"#form_id"%3Bs:9:"DrupalRCE"%3Bs:8:"#process"%3Ba:1:{i:0%3Bs:23:"drupal_process_attached"%3B}s:9:"#attached"%3Ba:1:{s:7:"phpinfo"%3Ba:1:{i:0%3Ba:1:{i:0%3Bs:1:"2"%3B}}}}}';
    $object = unserialize(urldecode($payload));

    // The object then needs to be destructed.
    unset($object);

    // If the exploit was successful, there should now be a row in cache_form.
    $payload2 = db_query_range('SELECT data FROM {cache_form} WHERE cid LIKE :cid', 0, 1, array(':cid' => 'form_DrupalRCE'))->fetchField();
    $this->assertFalse(is_string($payload2) && (strpos($payload2, 'phpinfo') !== FALSE), 'Second stage payload was not written to cache_form.');

    // The final exploit is executed via the ajax system, but is not a
    // sufficiently valid ajax form submission to use drupalPost for testing.
    $headers = array(
      'Content-Type: application/x-www-form-urlencoded',
    );
    $curl_options = array(
      CURLOPT_URL => url('system/ajax', array('absolute' => TRUE)),
      CURLOPT_POST => TRUE,
      CURLOPT_POSTFIELDS => 'form_build_id=DrupalRCE',
      CURLOPT_HTTPHEADER => $headers,
    );
    // The second stage payload causes several PHP warnings / notices if it is
    // there in cache_form.
    $content = $this->curlExec($curl_options);
    $this->assertFalse((strpos($content, 'Rasmus Lerdorf') !== FALSE), 'Remote Code Execution was not successful.');

    // Now opt-out of the cache_form protection.
    variable_set('drupal_cache_array_persist_cache_form', TRUE);
    $object = unserialize(urldecode($payload));

    // The object then needs to be destructed.
    unset($object);

    // If the exploit was successful, there should now be a row in cache_form.
    $payload2 = db_query_range('SELECT data FROM {cache_form} WHERE cid LIKE :cid', 0, 1, array(':cid' => 'form_DrupalRCE'))->fetchField();
    $this->assertTrue(is_string($payload2) && (strpos($payload2, 'phpinfo') !== FALSE), 'DrupalCacheArray persisted data to cache_form.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
