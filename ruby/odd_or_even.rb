def odd_or_even(array)
  sum=0
    array.each { |a| sum+=a }
    if sum % 2 == 0
    'even'
    else
    'odd'
    end
end