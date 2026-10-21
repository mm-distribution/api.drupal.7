# update_parse_xml()

- **Type:** Function
- **File:** [`modules/update/update.fetch.inc`](_file.md), lines 391–430 · [local source](../../../../source/modules/update/update.fetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc#L391-L430)
- **Module/theme:** update

## Signature

```php
function update_parse_xml($raw_xml)
```

## Documentation

```text
Parses the XML of the Drupal release history info files.

@param $raw_xml
  A raw XML string of available release data for a given project.

@return
  Array of parsed data about releases for a given project, or NULL if there
  was an error parsing the string.
```

## Code

```php
function update_parse_xml($raw_xml) {
  try {
    $xml = new SimpleXMLElement($raw_xml);
  }
  catch (Exception $e) {
    // SimpleXMLElement::__construct produces an E_WARNING error message for
    // each error found in the XML data and throws an exception if errors
    // were detected. Catch any exception and return failure (NULL).
    return;
  }
  // If there is no valid project data, the XML is invalid, so return failure.
  if (!isset($xml->short_name)) {
    return;
  }
  $short_name = (string) $xml->short_name;
  $data = array();
  foreach ($xml as $k => $v) {
    $data[$k] = (string) $v;
  }
  $data['releases'] = array();
  if (isset($xml->releases)) {
    foreach ($xml->releases->children() as $release) {
      $version = (string) $release->version;
      $data['releases'][$version] = array();
      foreach ($release->children() as $k => $v) {
        $data['releases'][$version][$k] = (string) $v;
      }
      $data['releases'][$version]['terms'] = array();
      if ($release->terms) {
        foreach ($release->terms->children() as $term) {
          if (!isset($data['releases'][$version]['terms'][(string) $term->name])) {
            $data['releases'][$version]['terms'][(string) $term->name] = array();
          }
          $data['releases'][$version]['terms'][(string) $term->name][] = (string) $term->value;
        }
      }
    }
  }
  return $data;
}
```

---
_Drupal 7.103 · [modules/update/update.fetch.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
