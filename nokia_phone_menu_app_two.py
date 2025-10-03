option = ""
while option != "14":
	main = """
		WELCOME TO THE NOKIA 3310 MENU
Below are the features offered:
	1. Phonebook
	2. Messages
	3. Chat
	4. Call register
	5. Tones
	6. Settings
	7. Call divert
	8. Games
	9. Calculator
	10. Reminders
	11. Clock 
	12. Profiles
	13. SIM services 
	14. exit		
	 """
	print(main)
	option = input("Enter a number: ")

	match option:
		case "1": 
			choice = ""
			while choice != "11" :
				phonebook = """
				Phonebook
				1. Search
				2. Service Nos.
				3. Add name
				4. Erase
				5. Edit
				6. Assign tone
				7. Send b'card
				8. Options
				9. Speed dials
				10. Voice tags
				11. previous
				"""
				print(phonebook)
				choice = input("Enter a number: ")
				match choice:
					case "11": print("Bye!")
					case "1": 
						searches = "" 
						while searches != "0":
							search = """
							Search
							0. back
								"""
							print(search)
							searches = input("Enter a number: ")
							match searches:
								case "0": print("Bye!")
								case _: print("Unsupported input!")

					case "2": 
						serve = "" 
						while serve != "0":
							service = """
							Service Nos.
							0. back
								"""
							print(service)
							serve = input("Enter a number: ")
							match serve:
								case "0": print("Bye!")
								case _: print("Unsupported input!")


					case "3": 
						add = "" 
						while add != "0":
							name = """
							Add name
							0. back
								"""
							print(name)
							add = input("Enter a number: ")
							match add:
								case "0": print("Bye!")
								case _: print("Unsupported input!")

	
					case "4": 
						erase = "" 
						while erase != "0":
							erases = """
							Erase
							0. back
								"""
							print(erases)
							erase = input("Enter a number: ")
							match erase:
								case "0": print("Bye!")
								case _: print("Unsupported input!")


					case "5":  
						edit = "" 
						while edit != "0":
							edits = """
							Edit
							0. back
								"""
							print(edits)
							edit = input("Enter a number: ")
							match edit:
								case "0": print("Bye!")
								case _: print("Unsupported input!")


					case "6":  
						asign = "" 
						while assign != "0":
							sign = """
							Assign tone
							0. back
								"""
							print(sign)
							assign = input("Enter a number: ")
							match assign:
								case "0": print("Bye!")
								case _: print("Unsupported input!")


					case "7":  
						send = "" 
						while send != "0":
							card = """
							Send b'card
							0. back
								"""
							print(card)
							send = input("Enter a number: ")
							match send:
								case "0": print("Bye!")
								case _: print("Unsupported input!")

					
					case "8": 
						picks = ""
						while picks != "3":
							choose = """
							1. Type of view
							2. Memory status
							3. return
							"""
							print(choose)
							picks = input("Enter a number: ")
							match picks:
								case "3": print("Bye!")
								case "1":  
									view = "" 
									while view != "0":
										types = """
											Type of view
											0. back
											"""
										print(types)
										view = input("Enter a number: ")
										match view:
											case "0": print("Bye!")
											case _: print("Unsupported input!")


								case "2":   
									mem = "" 
									while mem != "0":
										mems = """
											Type of view
											0. back
											"""
										print(mems)
										mem = input("Enter a number: ")
										match mem:
											case "0": print("Bye!")
											case _: print("Unsupported input!")


								case _: print("Unsupported input!")
					
					case "9":  
						speed = "" 
						while speed != "0":
							speedo = """
							Speed dials
							0. back
								"""
							print(speedo)
							speed = input("Enter a number: ")
							match speed:
								case "0": print("Bye!")
								case _: print("Unsupported input!")
					case "10": 
						tag = "" 
						while tag != "0":
							tags = """
							Voice tags
							0. back
								"""
							print(tags)
							tag = input("Enter a number: ")
							match tag:
								case "0": print("Bye!")
								case _: print("Unsupported input!")
					case _: print("Unsupported input!")

		case "2":
			pick = ""
			while pick != "11":
				messages = """
				1. Write messages
				2. Inbox
				3. Outbox
				4. Picture messages
				5. Templates
				6. Smileys
				7. Messages settings
				8. Info service
				9. Voice mailbox number
				10. Service command editor 
				11. back
				 """
				print(messages)
				pick = input("Enter a number: ")

				match pick:
					case "11" : print("Bye!")
					case "1": 
						write = "" 
						while write != "0":
							mess = """
							Write messages
							0. back
								"""
							print(mess)
							write = input("Enter a number: ")
							match write:
								case "0": print("Bye!")
								case _: print("Unsupported input!")
					case "2": 
						inbox = "" 
						while inbox != "0":
							box = """
							Inbox
							0. back
								"""
							print(box)
							inbox = input("Enter a number: ")
							match inbox:
								case "0": print("Bye!")
								case _: print("Unsupported input!")
					case "3": 
						out = "" 
						while out != "0":
							boxes = """
							Outbox
							0. back
								"""
							print(boxes)
							out = input("Enter a number: ")
							match out:
								case "0": print("Bye!")
								case _: print("Unsupported input!")		
					case "4": 
						pic = "" 
						while pic != "0":
							pics = """
							Picture messages
							0. back
								"""
							print(pics)
							pic = input("Enter a number: ")
							match pic:
								case "0": print("Bye!")
								case _: print("Unsupported input!")
					case "5":
						temp = "" 
						while temp != "0":
							plate = """
							Templates
							0. back
								"""
							print(plate)
							temp = input("Enter a number: ")
							match temp:
								case "0": print("Bye!")
								case _: print("Unsupported input!")
					case "6":
						smile = "" 
						while smile != "0":
							mile = """
							Smileys
							0. back
								"""
							print(mile)
							smile = input("Enter a number: ")
							match smile:
								case "0": print("Bye!")
								case _: print("Unsupported input!")
					case "7":
						set = ""
						while set != "3":
							message = """
							1. Set
							2. Common
							3. back
							"""
							print(message)
							set = input("Enter a number: ")
							match set:
								case "3" : print("Bye!")
								case "1":
									common = ""
									while common != "4":
										set_1 = """
										1. Message centre number
										2. Message sent as
										3. Message validity
										4. back
										"""
										print(set_1)		
										common = input("Enter a number: ")
										match common:
											case "4" : print("Bye!")
											case "1": 
												message = "" 
												while message != "0":
													centre = """
													Message centre number
													0. back
													"""
													print(centre)
													message = input("Enter a number: ")
													match message:
														case "0": print("Bye!")
														case _: print("Unsupported input!")
											case "2": 
												sent = "" 
												while sent != "0":
													send = """
													Message sent as
													0. back
													"""
													print(send)
													sent = input("Enter a number: ")
													match sent:
														case "0": print("Bye!")
														case _: print("Unsupported input!")

											case "3": 
												valid = "" 
												while valid != "0":
													validity = """
													Message validity
													0. back
													"""
													print(validity)
													valid = input("Enter a number: ")
													match valid:
														case "0": print("Bye!")
														case _: print("Unsupported input!")

											case _:  print("Unsupported input!")
									
								case "2":
									common_2 = ""
									while common_2 != "4":
										common_1 = """	
										1. Delivery reports
										2. Reply via same centre
										3. Character support
										4. previous
										"""
										print(common_1)
										common_2 = input("Enter a number: ")
										match common_2:
											case "4" : print("Bye!")
											case "1": 
												deliver = "" 
												while deliver != "0":
													rep = """
													Delivery reports
													0. back
													"""
													print(rep)
													deliver = input("Enter a number: ")
													match deliver:
														case "0": print("Bye!")
														case _: print("Unsupported input!")

											case "2": 
												reply = "" 
												while reply != "0":
													via = """
													Reply via same centre
													0. back
													"""
													print(via)
													reply = input("Enter a number: ")
													match reply:
														case "0": print("Bye!")
														case _: print("Unsupported input!")

											case "3": 
												character = "" 
												while character != "0":
													act = """
													Character support
													0. back
													"""
													print(act)
													character = input("Enter a number: ")
													match character:
														case "0": print("Bye!")
														case _: print("Unsupported input!")

											case _: print("Unsupported input!")
								
								case _: print("Unsupported input!")


					case "8":
						info = "" 
						while info != "0":
							serves = """
							Info services
							0. back
								"""
							print(serves)
							info = input("Enter a number: ")
							match info:
								case "0": print("Bye!")
								case _: print("Unsupported input!")
					case "9":
						mail = "" 
						while mail != "0":
							mailbox = """
							Voice mailbox number
							0. back
								"""
							print(mailbox)
							mail = input("Enter a number: ")
							match mail:
								case "0": print("Bye!")
								case _: print("Unsupported input!")
					case "10":
						service = "" 
						while service != "0":
							editor = """
							Service command editor
							0. back
								"""
							print(editor)
							service = input("Enter a number: ")
							match service:
								case "0": print("Bye!")
								case _: print("Unsupported input!")	
					case _: print("Unsupported input!")	
						


		case "3":
			hat = "" 
			while hat != "0":
				chat = """
				Chat
				0. back
				"""
				print(chat)
				hat = input("Enter a number: ")
				match hat:
					case "0": print("Bye!")
					case _: print("Unsupported input!")
		case "4":
			register = ""
			while register != "9":
				call = """
				1. Missed calls
				2. Received calls
				3. Dialled numbers
				4. Erase recent call lists
				5. Show call duration
				6. Show call costs
				7. Call cost settings
				8. Prepaid credit 
				9. return
				"""
				print(call)
				register = input("Enter a number: ")
				match register:
					case "9" : print("Bye!")
					case "1":
						miss = "" 
						while miss != "0":
							missed = """
							Missed calls
							0. back
								"""
							print(missed)
							miss = input("Enter a number: ")
							match miss:
								case "0": print("Bye!")
								case _: print("Unsupported input!")
					case "2":
						receive = "" 
						while receive != "0":
							received = """
							Received calls
							0. back
								"""
							print(received)
							receive = input("Enter a number: ")
							match receive:
								case "0": print("Bye!")
								case _: print("Unsupported input!")
					case "3":
						dial = "" 
						while dial != "0":
							dialled = """
							Dialled numbers
							0. back
								"""
							print(dialled)
							dial = input("Enter a number: ")
							match dial:
								case "0": print("Bye!")
								case _: print("Unsupported input!")		
					case "4":
						recent = "" 
						while recent != "0":
							cent = """
							Erase recent call lists
							0. back
								"""
							print(cent)
							recent = input("Enter a number: ")
							match recent:
								case "0": print("Bye!")
								case _: print("Unsupported input!")
					case "5":
						duration = ""
						while duration != "6":
							show = """
							1. Last call duration
							2. All calls' duration
							3. Received calls' duration
							4. Dialled calls' duration
							5. Clear timers 
							6. back
							"""
							print(show)
							duration = input("Enter a number: ")
							match duration:
								case "1":
									rate = "" 
									while rate != "0":
										last = """
										Last call duration
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "2":
									all = "" 
									while all != "0":
										duration = """
										All calls' duration
										0. back
										"""
										print(duration)
										all = input("Enter a number: ")
										match all:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "3":
									rec = "" 
									while rec != "0":
										ration = """
										Received calls' duration
										0. back
										"""
										print(ration)
										rec = input("Enter a number: ")
										match rec:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "4":
									rate = "" 
									while rate != "0":
										last = """
										Dialled calls' duration
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "5":
									clear = "" 
									while clear != "0":
										timer = """
										Clear timers
										0. back
										"""
										print(timer)
										clear = input("Enter a number: ")
										match clear:
											case "0": print("Bye!")
											case _: print("Unsupported input!")

								case _: print("Unsupported input!")	
							
					case "6":
						cost = ""
						while cost != "4":
							costs = """
							1. Last call cost
							2. All calls' cost
							3. Clear counters
							4. previous
							"""
							print(costs)
							cost = input("Enter a number: ")
							match cost:
								case "1":print("Last call cost")
								case "2":print("All calls' cost")
								case "3":print("Clear counters")
								case _: print("Unsupported input!")
					case "7":
						limit = ""
						while limit != "3":
							settings = """
							1. Call cost limit
							2. Show costs in
							3. previous
							"""
							print(settings)
							limit = input("Enter a number: ")
							match limit:
								case "1":print("Call cost limit")
								case "2":print("Show costs in")
								case _: print("Unsupported input!")
				
					case "8": 
						paid = "" 
						while paid != "0":
							credit = """
							Prepaid credit
							0. back
							"""
							print(credit)
							paid = input("Enter a number: ")
							match paid:
								case "0": print("Bye!")
								case _: print("Unsupported input!")
			
					case _: print("Unsupported input!")
		
		case "5":
			tone = ""
			while tone != "10":
				tones = """
				1. Ringing tone
				2. Ringing volume
				3. Incoming call alert
				4. Composer
				5. Message alert tone
				6. Keypad tones
				7. Warning and game tones
				8. Vibrating alert
				9. Screen saver
				10. return
				"""
				print(tones)
				tone = input("Enter a number: ")
				match tone:
					case "10":print("Bye!")
					case "1":
						rate = "" 
						while rate != "0":
							last = """
							Ringing tone
							0. back
							"""
							print(last)
							rate = input("Enter a number: ")
							match rate:
								case "0": print("Bye!")
								case _: print("Unsupported input!")

					case "2":
						rate = "" 
						while rate != "0":
							last = """
							Ringing volume
							0. back
							"""
							print(last)
							rate = input("Enter a number: ")
							match rate:
								case "0": print("Bye!")
								case _: print("Unsupported input!")


					case "3":
						rate = "" 
						while rate != "0":
							last = """
							Incoming call alert
							0. back
							"""
							print(last)
							rate = input("Enter a number: ")
							match rate:
								case "0": print("Bye!")
								case _: print("Unsupported input!")


					case "4":
						rate = "" 
						while rate != "0":
							last = """
							Composer
							0. back
							"""
							print(last)
							rate = input("Enter a number: ")
							match rate:
								case "0": print("Bye!")
								case _: print("Unsupported input!")


					case "5":
						rate = "" 
						while rate != "0":
							last = """
							Message alert tone
							0. back
							"""
							print(last)
							rate = input("Enter a number: ")
							match rate:
								case "0": print("Bye!")
								case _: print("Unsupported input!")


					case "6":
						rate = "" 
						while rate != "0":
							last = """
							Keypad tones
							0. back
							"""
							print(last)
							rate = input("Enter a number: ")
							match rate:
								case "0": print("Bye!")
								case _: print("Unsupported input!")


					case "7":
						rate = "" 
						while rate != "0":
							last = """
							Warning and game tones
							0. back
							"""
							print(last)
							rate = input("Enter a number: ")
							match rate:
								case "0": print("Bye!")
								case _: print("Unsupported input!")


					case "8":
						rate = "" 
						while rate != "0":
							last = """
							Vibrating alert
							0. back
							"""
							print(last)
							rate = input("Enter a number: ")
							match rate:
								case "0": print("Bye!")
								case _: print("Unsupported input!")


					case "9":
						rate = "" 
						while rate != "0":
							last = """
							Screen saver
							0. back
							"""
							print(last)
							rate = input("Enter a number: ")
							match rate:
								case "0": print("Bye!")
								case _: print("Unsupported input!")


					case _: print("Unsupported input!")
					
		case "6":	
			set = ""
			while set != "5":	
				setting = """
				1. Call settings
				2. Phone settings
				3. Security settings
				4. Restore factory settings
				5. return
				"""
				print(setting)
				set = input("Enter a number: ")
				match set:
					case "5": print("Bye!")
					case "1":
						auto = ""
						while auto != "7":
							automatic = """
							1. Automatic redial
							2. Speed dialling
							3. Call waiting options
							4. Own number sending
							5. Phone line in use
							6. Automatic answer
							7. back		
							"""
							print(automatic)
							auto = input("Enter a number: ")
							match auto:
								case "7": print("Bye!")
								case "1":
									rate = "" 
									while rate != "0":
										last = """
										Automatic redial
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")


								case "2":
									rate = "" 
									while rate != "0":
										last = """
										Speed dialling
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "3":
									rate = "" 
									while rate != "0":
										last = """
										Call waiting options
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "4":
									rate = "" 
									while rate != "0":
										last = """
										Own number sending
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "5":
									rate = "" 
									while rate != "0":
										last = """
										Phone line in use
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "6":
									rate = "" 
									while rate != "0":
										last = """
										Automatic answer
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case _: print("Unsupported input!")		
							
					case "2":
						language = ""
						while language != "7":
							phone = """
							1. Language
							2. Cell info display
							3. Welcome note
							4. Network selection
							5. Lights
							6. Confirm SIM service actions
							7. back
							"""
							print(phone)
							language = input("Enter a number:")
							match language:
								case "7": print("Bye!")
								case "1":
									rate = "" 
									while rate != "0":
										last = """
										Language
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "2":
									rate = "" 
									while rate != "0":
										last = """
										Cell info display
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "3":
									rate = "" 
									while rate != "0":
										last = """
										Welcome note
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "4":
									rate = "" 
									while rate != "0":
										last = """
										Network selection
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "5":
									rate = "" 
									while rate != "0":
										last = """
										Lights
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "6":
									rate = "" 
									while rate != "0":
										last = """
										Confirm SIM service actions
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case _: print("Unsupported input!")								
	
		
					case "3":
						secure = ""
						while secure != "7":
							security = """
							1. PIN code request
							2. Call barring service
							3. Fixed dialling
							4. Closed user group
							5. Phone security
							6. Change access codes
							7. back
							"""
							print(security)
							secure = input("Enter a number: ")
							match secure:
								case "7": print("Bye!")
								case "1":
									rate = "" 
									while rate != "0":
										last = """
										PIN code request
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "2":
									rate = "" 
									while rate != "0":
										last = """
										Call barring service
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "3":
									rate = "" 
									while rate != "0":
										last = """
										Fixed dialling
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "4":
									rate = "" 
									while rate != "0":
										last = """
										Closed user group
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "5":
									rate = "" 
									while rate != "0":
										last = """
										Phone security
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case "6":
									rate = "" 
									while rate != "0":
										last = """
										Change access codes
										0. back
										"""
										print(last)
										rate = input("Enter a number: ")
										match rate:
											case "0": print("Bye!")
											case _: print("Unsupported input!")
								case _: print("Unsupported input!")
									
					case "4":
						rate = "" 
						while rate != "0":
							last = """
							Restore factory settings
							0. back
							"""
							print(last)
							rate = input("Enter a number: ")
							match rate:
								case "0": print("Bye!")
								case _: print("Unsupported input!")
					case _: print("Unsupported input!")	
				
		case "7":
			rate = "" 
			while rate != "0":
				last = """
				Call divert
				0. back
				"""
				print(last)
				rate = input("Enter a number: ")
				match rate:
					case "0": print("Bye!")
					case _: print("Unsupported input!")
		case "8":
			rate = "" 
			while rate != "0":
				last = """
				Games
				0. back
				"""
				print(last)
				rate = input("Enter a number: ")
				match rate:
					case "0": print("Bye!")
					case _: print("Unsupported input!")

		case "9":
			rate = "" 
			while rate != "0":
				last = """
				Calculator
				0. back
				"""
				print(last)
				rate = input("Enter a number: ")
				match rate:
					case "0": print("Bye!")
					case _: print("Unsupported input!")

		case "10":
			rate = "" 
			while rate != "0":
				last = """
				Reminders
				0. back
				"""
				print(last)
				rate = input("Enter a number: ")
				match rate:
					case "0": print("Bye!")
					case _: print("Unsupported input!")

		case "11":
			alarm = ""
			while alarm != "7":
				clock = """
				1. Alarm clock
				2. Clock settings
				3. Date settings
				4. Stopwatch
				5. Countdown timer
				6. Auto update of date and time
				7. previous
				"""
				print(clock)
				alarm = input("Enter a number: ")
				match alarm:
					case "7": print("Bye!")
					case "1":
						rate = "" 
						while rate != "0":
							last = """
							Alarm clock
							0. back
							"""
							print(last)
							rate = input("Enter a number: ")
							match rate:
								case "0": print("Bye!")
								case _: print("Unsupported input!")

					case "2":
						rate = "" 
						while rate != "0":
							last = """
							Clock settings
							0. back
							"""
							print(last)
							rate = input("Enter a number: ")
							match rate:
								case "0": print("Bye!")
								case _: print("Unsupported input!")

					case "3":
						rate = "" 
						while rate != "0":
							last = """
							Date settings
							0. back
							"""
							print(last)
							rate = input("Enter a number: ")
							match rate:
								case "0": print("Bye!")
								case _: print("Unsupported input!")

					case "4":
						rate = "" 
						while rate != "0":
							last = """
							Stopwatch
							0. back
							"""
							print(last)
							rate = input("Enter a number: ")
							match rate:
								case "0": print("Bye!")
								case _: print("Unsupported input!")

					case "5":
						rate = "" 
						while rate != "0":
							last = """
							Countdown timer
							0. back
							"""
							print(last)
							rate = input("Enter a number: ")
							match rate:
								case "0": print("Bye!")
								case _: print("Unsupported input!")

					case "6":
						rate = "" 
						while rate != "0":
							last = """
							Auto update of date and time
							0. back
							"""
							print(last)
							rate = input("Enter a number: ")
							match rate:
								case "0": print("Bye!")
								case _: print("Unsupported input!")

					case _: print("Unsupported input!")
							
		case "12":
			rate = "" 
			while rate != "0":
				last = """
				Profiles
				0. back
				"""
				print(last)
				rate = input("Enter a number: ")
				match rate:
					case "0": print("Bye!")
					case _: print("Unsupported input!")

		case "13":
			rate = "" 
			while rate != "0":
				last = """
				SIM services
				0. back
				"""
				print(last)
				rate = input("Enter a number: ")
				match rate:
					case "0": print("Bye!")
					case _: print("Unsupported input!")

		case "14":print("Goodbye!")
		case _: print("Unsupported input!")
