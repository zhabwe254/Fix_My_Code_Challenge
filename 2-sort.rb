#!/usr/bin/env ruby

require 'optparse'

# Define default behavior: sort ascending, start from first argument
options = {}
OptionParser.new do |opts|
  opts.on('-d', '--descending', 'Sort in descending order (default: ascending)') { |v| options[:descending] = true }
  opts.on('-s', '--start', Integer, 'Index of the first argument to sort (default: 1)') { |v| options[:start] = v }
end.parse!

# Extract valid integer arguments starting from specified index
arguments = ARGV[options[:start] - 1..-1].select { |arg| arg =~ /^-?[0-9]+$/ }.map(&:to_i)

# Sort based on desired order
sorted_arguments = options[:descending] ? arguments.sort { |a, b| b <=> a } : arguments.sort

# Print the sorted arguments
puts sorted_arguments.join(' ')
