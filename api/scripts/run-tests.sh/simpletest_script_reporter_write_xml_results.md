# simpletest_script_reporter_write_xml_results()

- **Type:** Function
- **File:** [`scripts/run-tests.sh`](_file.md), lines 664–729 · [local source](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh#L664-L729)

## Signature

```php
function simpletest_script_reporter_write_xml_results()
```

## Documentation

```text
Display jUnit XML test results.
```

## Code

```php
function simpletest_script_reporter_write_xml_results() {
  global $args, $test_id, $results_map;

  $results = db_query("SELECT * FROM {simpletest} WHERE test_id = :test_id ORDER BY test_class, message_id", array(':test_id' => $test_id));

  $test_class = '';
  $xml_files = array();

  foreach ($results as $result) {
    if (isset($results_map[$result->status])) {
      if ($result->test_class != $test_class) {
        // We've moved onto a new class, so write the last classes results to a file:
        if (isset($xml_files[$test_class])) {
          file_put_contents($args['xml'] . '/' . $test_class . '.xml', $xml_files[$test_class]['doc']->saveXML());
          unset($xml_files[$test_class]);
        }
        $test_class = $result->test_class;
        if (!isset($xml_files[$test_class])) {
          $doc = new DomDocument('1.0');
          $root = $doc->createElement('testsuite');
          $root = $doc->appendChild($root);
          $xml_files[$test_class] = array('doc' => $doc, 'suite' => $root);
        }
      }

      // For convenience:
      $dom_document = &$xml_files[$test_class]['doc'];

      // Create the XML element for this test case:
      $case = $dom_document->createElement('testcase');
      $case->setAttribute('classname', $test_class);
      list($class, $name) = explode('->', $result->function, 2);
      $case->setAttribute('name', $name);

      // Passes get no further attention, but failures and exceptions get to add more detail:
      if ($result->status == 'fail') {
        $fail = $dom_document->createElement('failure');
        $fail->setAttribute('type', 'failure');
        $fail->setAttribute('message', $result->message_group);
        $text = $dom_document->createTextNode($result->message);
        $fail->appendChild($text);
        $case->appendChild($fail);
      }
      elseif ($result->status == 'exception') {
        // In the case of an exception the $result->function may not be a class
        // method so we record the full function name:
        $case->setAttribute('name', $result->function);

        $fail = $dom_document->createElement('error');
        $fail->setAttribute('type', 'exception');
        $fail->setAttribute('message', $result->message_group);
        $full_message = $result->message . "\n\nline: " . $result->line . "\nfile: " . $result->file;
        $text = $dom_document->createTextNode($full_message);
        $fail->appendChild($text);
        $case->appendChild($fail);
      }
      // Append the test case XML to the test suite:
      $xml_files[$test_class]['suite']->appendChild($case);
    }
  }
  // The last test case hasn't been saved to a file yet, so do that now:
  if (isset($xml_files[$test_class])) {
    file_put_contents($args['xml'] . '/' . $test_class . '.xml', $xml_files[$test_class]['doc']->saveXML());
    unset($xml_files[$test_class]);
  }
}
```

---
_Drupal 7.103 · [scripts/run-tests.sh](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · Licensed GPL-2.0-or-later (see LICENSE)._
