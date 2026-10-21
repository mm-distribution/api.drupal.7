# BootstrapDestinationTestCase::testDestination()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 850–905 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L850-L905)
- **Class:** [BootstrapDestinationTestCase](../BootstrapDestinationTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testDestination()
```

## Documentation

```text
Tests that $_GET/$_REQUEST['destination'] only contain internal URLs.

@see _drupal_bootstrap_variables()
@see system_test_get_destination()
@see system_test_request_destination()
```

## Code

```php
  public function testDestination() {
    $test_cases = array(
      array(
        'input' => 'node',
        'output' => 'node',
        'message' => "Standard internal example node path is present in the 'destination' parameter.",
      ),
      array(
        'input' => '/example.com',
        'output' => '/example.com',
        'message' => 'Internal path with one leading slash is allowed.',
      ),
      array(
        'input' => '//example.com/test',
        'output' => '',
        'message' => 'External URL without scheme is not allowed.',
      ),
      array(
        'input' => 'example:test',
        'output' => 'example:test',
        'message' => 'Internal URL using a colon is allowed.',
      ),
      array(
        'input' => 'http://example.com',
        'output' => '',
        'message' => 'External URL is not allowed.',
      ),
      array(
        'input' => 'javascript:alert(0)',
        'output' => 'javascript:alert(0)',
        'message' => 'Javascript URL is allowed because it is treated as an internal URL.',
      ),
    );
    foreach ($test_cases as $test_case) {
      // Test $_GET['destination'].
      $this->drupalGet('system-test/get-destination', array('query' => array('destination' => $test_case['input'])));
      $this->assertIdentical($test_case['output'], $this->drupalGetContent(), $test_case['message']);
      // Test $_REQUEST['destination']. There's no form to submit to, so
      // drupalPost() won't work here; this just tests a direct $_POST request
      // instead.
      $curl_parameters = array(
        CURLOPT_URL => $this->getAbsoluteUrl('system-test/request-destination'),
        CURLOPT_POST => TRUE,
        CURLOPT_POSTFIELDS => 'destination=' . urlencode($test_case['input']),
        CURLOPT_HTTPHEADER => array(),
      );
      $post_output = $this->curlExec($curl_parameters);
      $this->assertIdentical($test_case['output'], $post_output, $test_case['message']);
    }

    // Make sure that 404 pages do not populate $_GET['destination'] with
    // external URLs.
    variable_set('site_404', 'system-test/get-destination');
    $this->drupalGet('http://example.com', array('external' => FALSE));
    $this->assertIdentical('', $this->drupalGetContent(), 'External URL is not allowed on 404 pages.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
