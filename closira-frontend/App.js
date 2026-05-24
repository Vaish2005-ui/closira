import React from 'react';

import {
  View,
  Text,
  FlatList,
  TouchableOpacity,
  StyleSheet
} from 'react-native';

import { NavigationContainer } from '@react-navigation/native';

import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

import { createNativeStackNavigator } from '@react-navigation/native-stack';


const Tab = createBottomTabNavigator();
const Stack = createNativeStackNavigator();


const leads = [

  {
    id: '1',
    customer: 'Sarah M.',
    channel: 'WhatsApp',
    status: 'Escalated',
    message: 'I am unhappy with pricing',
    summary: 'Customer requested manager support.',
    time: '10:30 AM'
  },

  {
    id: '2',
    customer: 'Rahul',
    channel: 'Email',
    status: 'Qualified',
    message: 'Need booking details',
    summary: 'Interested in booking services.',
    time: '11:15 AM'
  },

  {
    id: '3',
    customer: 'Emily',
    channel: 'Instagram',
    status: 'Follow-up',
    message: 'Need product demo',
    summary: 'Requested callback tomorrow.',
    time: '1:00 PM'
  }

];



function DashboardScreen() {

  return (

    <View style={styles.container}>

      <Text style={styles.mainTitle}>
        Closira Dashboard
      </Text>

      <View style={styles.statCard}>
        <Text style={styles.statNumber}>24</Text>
        <Text>Total Leads Today</Text>
      </View>

      <View style={styles.statCard}>
        <Text style={styles.statNumber}>5</Text>
        <Text>Open Escalations</Text>
      </View>

      <View style={styles.statCard}>
        <Text style={styles.statNumber}>8</Text>
        <Text>Follow-ups Due</Text>
      </View>

      <Text style={styles.sectionTitle}>
        Recent Activity
      </Text>

      <View style={styles.activityCard}>
        <Text>Sarah M. enquiry escalated</Text>
      </View>

      <View style={styles.activityCard}>
        <Text>Rahul marked as qualified lead</Text>
      </View>

    </View>
  );
}



function LeadsScreen({ navigation }) {

  return (

    <View style={styles.container}>

      <FlatList
        data={leads}
        keyExtractor={(item) => item.id}

        renderItem={({ item }) => (

          <TouchableOpacity
            style={styles.leadCard}

            onPress={() =>
              navigation.navigate(
                'Conversation',
                { lead: item }
              )
            }
          >

            <Text style={styles.customerName}>
              {item.customer}
            </Text>

            <Text>
              Channel: {item.channel}
            </Text>

            <Text>
              Status: {item.status}
            </Text>

            <Text>
              Time: {item.time}
            </Text>

          </TouchableOpacity>

        )}
      />

    </View>
  );
}



function ConversationScreen({ route }) {

  const { lead } = route.params;

  return (

    <View style={styles.container}>

      <Text style={styles.mainTitle}>
        {lead.customer}
      </Text>

      <View style={styles.detailCard}>

        <Text style={styles.label}>
          Channel
        </Text>

        <Text>
          {lead.channel}
        </Text>

      </View>

      <View style={styles.detailCard}>

        <Text style={styles.label}>
          Status
        </Text>

        <Text>
          {lead.status}
        </Text>

      </View>

      <View style={styles.detailCard}>

        <Text style={styles.label}>
          Message
        </Text>

        <Text>
          {lead.message}
        </Text>

      </View>

      <View style={styles.detailCard}>

        <Text style={styles.label}>
          AI Summary
        </Text>

        <Text>
          {lead.summary}
        </Text>

      </View>

    </View>
  );
}



function EscalationScreen() {

  const escalations = leads.filter(
    (item) => item.status === 'Escalated'
  );

  return (

    <View style={styles.container}>

      <Text style={styles.mainTitle}>
        Escalations
      </Text>

      <FlatList
        data={escalations}
        keyExtractor={(item) => item.id}

        renderItem={({ item }) => (

          <View style={styles.escalationCard}>

            <Text style={styles.customerName}>
              {item.customer}
            </Text>

            <Text>
              {item.message}
            </Text>

          </View>

        )}
      />

    </View>
  );
}



function FollowUpScreen() {

  const followups = leads.filter(
    (item) => item.status === 'Follow-up'
  );

  return (

    <View style={styles.container}>

      <Text style={styles.mainTitle}>
        Follow-ups
      </Text>

      <FlatList
        data={followups}
        keyExtractor={(item) => item.id}

        renderItem={({ item }) => (

          <View style={styles.followupCard}>

            <Text style={styles.customerName}>
              {item.customer}
            </Text>

            <Text>
              Follow-up scheduled
            </Text>

          </View>

        )}
      />

    </View>
  );
}



function LeadStack() {

  return (

    <Stack.Navigator>

      <Stack.Screen
        name="LeadsMain"
        component={LeadsScreen}
        options={{ title: 'Leads' }}
      />

      <Stack.Screen
        name="Conversation"
        component={ConversationScreen}
      />

    </Stack.Navigator>

  );
}



export default function App() {

  return (

    <NavigationContainer>

      <Tab.Navigator>

        <Tab.Screen
          name="Dashboard"
          component={DashboardScreen}
        />

        <Tab.Screen
          name="Leads"
          component={LeadStack}
          options={{ headerShown: false }}
        />

        <Tab.Screen
          name="Escalations"
          component={EscalationScreen}
        />

        <Tab.Screen
          name="FollowUps"
          component={FollowUpScreen}
        />

      </Tab.Navigator>

    </NavigationContainer>

  );
}



const styles = StyleSheet.create({

  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f8fafc'
  },

  mainTitle: {
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 20
  },

  statCard: {
    backgroundColor: '#ffffff',
    padding: 20,
    borderRadius: 16,
    marginBottom: 15,
  
    shadowColor: '#000',
    shadowOpacity: 0.05,
    shadowRadius: 10,
  
    elevation: 3
  },  

  statNumber: {
    fontSize: 28,
    fontWeight: 'bold'
  },

  sectionTitle: {
    fontSize: 22,
    fontWeight: 'bold',
    marginTop: 20,
    marginBottom: 15
  },

  activityCard: {
    backgroundColor: '#f7f7f7',
    padding: 18,
    borderRadius: 12,
    marginBottom: 10
  },

  leadCard: {
    backgroundColor: '#f2f2f2',
    padding: 20,
    borderRadius: 16,
    marginBottom: 15
  },

  customerName: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 8
  },

  detailCard: {
    backgroundColor: '#f2f2f2',
    padding: 20,
    borderRadius: 16,
    marginBottom: 15
  },

  label: {
    fontWeight: 'bold',
    marginBottom: 8
  },

  escalationCard: {
    backgroundColor: '#ffe5e5',
    padding: 20,
    borderRadius: 16,
    marginBottom: 15
  },

  followupCard: {
    backgroundColor: '#e8f5e9',
    padding: 20,
    borderRadius: 16,
    marginBottom: 15
  }

});